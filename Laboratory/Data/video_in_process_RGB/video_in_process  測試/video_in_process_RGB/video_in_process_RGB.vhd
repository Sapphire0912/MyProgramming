library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.all;

entity video_in_process_RGB is
port(
    rst              : in std_logic;
------------video_in_I2C---------------------------------
    video_clk        : in std_logic;
    video_sda        : inout std_logic;
    video_scl        : inout std_logic;
    video_data_I2C   : in std_logic_vector(7 downto 0);
------------video_out & VGA CNT---------------------------------
    vga_vs_cnt       : out integer;
    vga_hs_cnt       : out integer;
    hsync            : out std_logic;
    vsync            : out std_logic;
    Frame_ID         : out std_logic;
    video_gray_out   : out std_logic_vector(7 downto 0);
    video_r_out      : out std_logic_vector(7 downto 0);
    video_g_out      : out std_logic_vector(7 downto 0);
    video_b_out      : out std_logic_vector(7 downto 0)
);
end video_in_process_RGB;

architecture Behavioral of video_in_process_RGB is
----------------------------------------
signal Cb_register, Cr_register : std_logic_vector(7 downto 0);
constant YCR_C1 : std_logic_vector(11 downto 0):=x"5a1";--constant1 of YUV convert R, 1.4075(d) * 1024(d) = 5a1(H)
constant YCG_C1 : std_logic_vector(11 downto 0):=x"161";--constant1 of YUV convert G, 0.3455(d) * 1024(d) = 161(H)
constant YCG_C2 : std_logic_vector(11 downto 0):=x"2de";--constant2 of YUV convert G, 0.7169(d) * 1024(d) = 2de(H)
constant YCB_C1 : std_logic_vector(11 downto 0):=x"71d";--constant1 of YUV convert B, 1.7790(d) * 1024(d) = 71d(H)
signal YCR : std_logic_vector(19 downto 0);
signal YCG : std_logic_vector(19 downto 0);
signal YCB : std_logic_vector(19 downto 0);
signal vsync_s : std_logic;
----------------------------------------I2C
component i2c
    Port (
        clk : in  std_logic;                   
        rst : in  std_logic;
        sda : inout std_logic;
        scl : inout std_logic
    );
end component;
----------------------------------------VGA
signal vga_hs_cnt_s : integer ;
signal vga_vs_cnt_s : integer ;
signal Frame_ID_s   : std_logic ;
component VGA
    generic(
        horizontal_resolution : integer :=1280 ;
        horizontal_Front_porch: integer :=  48 ;
        horizontal_Sync_pulse : integer := 112 ;
        horizontal_Back_porch : integer := 248 ;
        h_sync_Polarity       :std_logic:= '1' ;
        vertical_resolution   : integer :=1024 ;
        vertical_Front_porch  : integer :=   1 ;
        vertical_Sync_pulse   : integer :=   3 ;
        vertical_Back_porch   : integer :=  38 ;
        v_sync_Polarity       :std_logic:= '1' 
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        video_start_en : in std_logic;
        vga_hs_cnt : out integer ;
        vga_vs_cnt : out integer ;
        hsync : out std_logic;
        vsync : out std_logic
    );
end component;
----------------------------------------
signal video_error : std_logic;
----------------------------------------camera
signal video_start_en : std_logic ;
signal cnt_video_hsync : integer range 0 to 1715;
----------------------------------------
signal buf_vga_state : std_logic_vector(1 downto 0);
signal buf_vga_Y_in_cnt : integer range 0 to 719;
----------------------------------------
type Array_type_8 is ARRAY (integer range 0 to 719) of std_logic_vector(7 downto 0);
signal buf_video_data : Array_type_8;
signal buf_vga_R      : Array_type_8;
signal buf_vga_G      : Array_type_8;
signal buf_vga_B      : Array_type_8;
----------------------------------------video_in
component video_in
    port(
        clk : in std_logic;    
        rst : in  std_logic;
        video_data : in std_logic_vector(7 downto 0);
        video_start_en : out std_logic ;
        cnt_video_hsync : out integer range 0 to 1715
    );
end component;
----------------------------------------
begin----------------------------------------
----------------------------------------i2c
i2c_1 :i2c
    PORT MAP (
         clk => video_clk,
         rst => video_error,
         sda => video_sda,
         scl => video_scl
    );
----------------------------------------video_in
video_in_1 :video_in
    PORT MAP (
        clk            => video_clk,
        rst            => video_error,
        video_data     => video_data_I2C,
        video_start_en => video_start_en,
        cnt_video_hsync=> cnt_video_hsync
    );
----------------------------------------
process(video_error, video_clk)
begin
if video_error = '0' then
	buf_vga_state <= "00";
	buf_vga_Y_in_cnt <= 0;
	
	YCR <= x"00000"; --YUV convert R
	YCG <= x"00000"; --YUV convert G
	YCB <= x"00000"; --YUV convert B
	
	Cr_register <= x"00";
	Cb_register <= x"00";
else
	if rising_edge(video_clk) then
		if (cnt_video_hsync>=0 and cnt_video_hsync < 1439 and video_start_en = '1') then
			case buf_vga_state(0) is
				when '0' =>	 buf_vga_state <= buf_vga_state + "01"; --the vdata is Cb
					if YCR > x"00000" or YCG > x"00000" or YCB > x"00000" then	--The first data has not yet completed calculate
						if YCR(18) = '1' or YCR(19) = '1' then
							buf_vga_R(buf_vga_Y_in_cnt) <= "11111111";
						else
							buf_vga_R(buf_vga_Y_in_cnt) <= YCR(17 downto 10);
						end if;
						if YCG(18) = '1' or YCG(19) = '1' then
							buf_vga_G(buf_vga_Y_in_cnt) <= "11111111";
						else
							buf_vga_G(buf_vga_Y_in_cnt) <= YCG(17 downto 10);
						end if;
						if YCB(18) = '1' or YCB(19) = '1' then
							buf_vga_B(buf_vga_Y_in_cnt) <= "11111111";
						else
							buf_vga_B(buf_vga_Y_in_cnt) <= YCB(17 downto 10);
						end if;

					end if;
					
					--cb
					if buf_vga_state(1)='0' then
						Cb_register <= video_data_I2C;
						YCR <= Cr_register * YCR_C1;
						YCG <= video_data_I2C * YCG_C1 + Cr_register * YCG_C2;
						YCB <= video_data_I2C * YCB_C1;
					--cr
					else
						Cr_register <= video_data_I2C;
						YCR <= video_data_I2C * YCR_C1;
						YCG <= Cb_register * YCG_C1 + video_data_I2C * YCG_C2;
						YCB <= Cb_register * YCB_C1;
					end if;
				when '1' =>		buf_vga_state <= buf_vga_state + "01"; --the vdata is Y
					--x"400"   = 1024(d)
					--x"2d0a3" = 1024(d) * 128(d) * 1.4075(d)
					--x"b0e5"  = 1024(d) * 128(d) * 0.3455(d)
					--x"16f0d" = 1024(d) * 128(d) * 0.7169(d)
					--x"38ed9" = 1024(d) * 128(d) * 1.7790(d)
--									YCR <= YCR + vdata * x"400" - x"2d0a3";
--									YCG <= (YCG xor x"fffff") + vdata * x"400" + x"b0e5" + x"16f0d";
--									YCB <= YCB + vdata * x"400" - x"38ed9";

					if YCR + video_data_I2C * x"400" < x"2d0a3" then
						YCR <= x"00000";
					else
						YCR <= YCR + video_data_I2C * x"400" - x"2d0a3";
					end if;
					
					if YCG > video_data_I2C * x"400" + x"b0e5" + x"16f0d" then
						YCG <= x"00000";
					else
						YCG <=  video_data_I2C * x"400" + x"b0e5" + x"16f0d" - YCG;
					end if;
					
					if YCB + video_data_I2C * x"400" < x"38ed9" then
						YCB <= x"00000";
					else
						YCB <= YCB + video_data_I2C * x"400" - x"38ed9";
					end if;
					
					if buf_vga_Y_in_cnt = 719 then
						buf_vga_Y_in_cnt <= 0;
					else
						buf_vga_Y_in_cnt <= buf_vga_Y_in_cnt + 1;
					end if;
					buf_video_data(buf_vga_Y_in_cnt) <= video_data_I2C;
				when others => null;
			end case;
		else
			buf_vga_state <= "00";
			buf_vga_Y_in_cnt <= 0;
			YCR <= x"00000";
			YCG <= x"00000";
			YCB <= x"00000";
		end if;
	end if;
end if;
end process;
----------------------------------------
--H equals 1 always indicates EAV.
--
--H equals 0 always indicates SAV. 
--
--The alignment of V and F to the line and  field counter varies depending on the standard.
--
--P3 = V xor H
--P2 = F xor H
--P1 = F xor V
--P0 = F xor V xor H
--
--EAV and SAV Sequence
--8-BIT DATA:(MSB)D7 D6 D5 D4 D3 D2 D1 D0
--Preamble         1  1  1  1  1  1  1  1
--Preamble         0  0  0  0  0  0  0  0
--Preamble         0  0  0  0  0  0  0  0
--Status word      1  F  V  H P3 P2 P1 P0
--
process(rst, video_clk)
begin
if rst = '0' then
    video_error<='0';
else
    if rising_edge(video_clk) then
	 	  if(
	 	         (cnt_video_hsync = 1440 and video_data_I2C   /= x"ff")
            or (cnt_video_hsync = 1441 and video_data_I2C   /= x"00")
--	 	        or (cnt_video_hsync = 1712 and video_data_I2C   /= x"ff")
--            or (cnt_video_hsync = 1713 and video_data_I2C   /= x"00")
--            or (cnt_video_hsync = 1714 and video_data_I2C   /= x"00")
            or (cnt_video_hsync = 1715 and video_data_I2C(5) = '1' and vga_vs_cnt_s < 480)
        ) then
            video_error<='0';
        else
            video_error<='1';
        end if;
    end if;
end if;
end process;
----------------------------------------VGA
VGA_1: VGA
    generic map(
        horizontal_resolution => 720 ,
        horizontal_Front_porch=>  16 ,
        horizontal_Sync_pulse =>  62 ,
        horizontal_Back_porch =>  59 ,
        h_sync_Polarity       => '1' ,
        vertical_resolution   => 480 ,
        vertical_Front_porch  =>   9 ,
        vertical_Sync_pulse   =>   6 ,
        vertical_Back_porch   =>  29 ,
        v_sync_Polarity       => '1' 
    )
    port map(
        clk =>video_clk ,
        rst =>video_error,
        video_start_en =>video_start_en,
        vga_hs_cnt =>vga_hs_cnt_s,
        vga_vs_cnt =>vga_vs_cnt_s,
        hsync      =>hsync,
        vsync      =>vsync_s
    );
vsync<=vsync_s;
vga_hs_cnt<=vga_hs_cnt_s;
vga_vs_cnt<=vga_vs_cnt_s;
----------------------------------------
process(video_error , vsync_s)
begin
if video_error = '0' then
    Frame_ID_s<='0';
else
    if falling_edge(vsync_s) then
        Frame_ID_s<=not(Frame_ID_s);
    end if;
end if;
end process;
Frame_ID<=Frame_ID_s;
----------------------------------------
process(video_error, video_clk)
begin
if video_error = '0' then
    video_gray_out<="00000000";
    video_r_out   <="00000000";
    video_g_out   <="00000000";
    video_b_out   <="00000000";
else
    if rising_edge(video_clk) then
        if (vga_hs_cnt_s<720 and vga_vs_cnt_s<480 and video_start_en = '1') then
            video_gray_out<=buf_video_data(    vga_hs_cnt_s);
            video_r_out   <=buf_vga_R     (    vga_hs_cnt_s);
            video_g_out   <=buf_vga_G     (    vga_hs_cnt_s);
            video_b_out   <=buf_vga_B     (    vga_hs_cnt_s);
        else
            video_gray_out<="00000000";
            video_r_out   <="00000000";
            video_g_out   <="00000000";
            video_b_out   <="00000000";
        end if;
    end if;
end if;
end process;
----------------------------------------
end architecture;