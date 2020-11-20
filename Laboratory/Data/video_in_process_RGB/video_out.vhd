library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
--use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.all;

entity video_out is
port(
    
    reset            : in std_logic;
--------set---------------------------------
    mode_sw        : in std_logic;--
------------video in I2C---------------------------------
    video_clk      : in std_logic;
    video_sda      : inout std_logic;
    video_scl      : inout std_logic;
    video_data_i2c : in std_logic_vector(7 downto 0);
------------vga---------------------------------
	rgb_out          : out std_logic_vector(7 downto 0); --
	led1            : out std_logic;
    --Rout          : out std_logic_vector(7 downto 0); --
    --Gout          : out std_logic_vector(7 downto 0); --
    --Bout          : out std_logic_vector(7 downto 0); --
    hsync          : out std_logic;
    vsync          : out std_logic
);
end video_out;

architecture Behavioral of video_out is
----------------------------------------VGA---------------------------
signal video_gray_out : std_logic_vector(7 downto 0);
signal video_r_out    : std_logic_vector(7 downto 0);
signal video_g_out    : std_logic_vector(7 downto 0);
signal video_b_out    : std_logic_vector(7 downto 0);

signal r : std_logic_vector(7 downto 0);
signal g : std_logic_vector(7 downto 0);
signal b : std_logic_vector(7 downto 0);
----------------------------------------VGA---------------------------
signal vga_vs_cnt : integer ;
signal vga_hs_cnt : integer ;
signal Frame_ID         : std_logic ;
signal rst         : std_logic ;
signal video_start_en_s : std_logic ;
----------------------------------------影像---------------------------
component video_in_process_RGB        
port(
    rst              : in std_logic;
------------video_in_I2C---------------------------------
    video_clk        : in std_logic;
    video_sda        : inout std_logic;
    video_scl        : inout std_logic;
    video_data_i2c   : in std_logic_vector(7 downto 0);
------------video_out & VGA CNT---------------------------------
    vga_vs_cnt       : out integer;
    vga_hs_cnt       : out integer;
    hsync            : out std_logic;
    vsync            : out std_logic;
    Frame_ID         : out std_logic;
    video_gray_out   : out std_logic_vector(7 downto 0);
    video_r_out      : out std_logic_vector(7 downto 0);
    video_g_out      : out std_logic_vector(7 downto 0);
    video_b_out      : out std_logic_vector(7 downto 0);
	video_start_en_s : out std_logic
);
end component;
-------------------------------------------- --------------------------------------------
begin
-------------------------------------------- --------------------------------------------
rst <= not reset;
----------------------------------------影像---------------------------
video_in_process_RGB_Front :video_in_process_RGB  
Port MAP( 
    rst              => rst,
    video_clk        => video_clk,
    video_sda        => video_sda,
    video_scl        => video_scl,
    video_data_i2c   => video_data_i2c,
    vga_vs_cnt       => vga_vs_cnt,
    vga_hs_cnt       => vga_hs_cnt,
    hsync            => hsync,
    vsync            => vsync,
    Frame_ID         => Frame_ID,
    video_gray_out   => video_gray_out,
    video_r_out      => video_r_out   ,
    video_g_out      => video_g_out   ,
    video_b_out      => video_b_out	,
	video_start_en_s =>	video_start_en_s
);
    rgb_out <= video_gray_out; --
----------------------------------------vga out 狀態機動作----------------------------------------
process( rst , video_clk    ,vga_hs_cnt , vga_vs_cnt )
begin
if rst = '0' then
    r <= "00000000";
    g <= "00000000";
    b <= "00000000";
	
elsif rising_edge(video_clk) then
    if (vga_hs_cnt < 720  and vga_vs_cnt < 480 ) then
		if (mode_sw='1') then   
            r <= video_r_out;         
            g <= video_g_out;         
            b <= video_b_out;         
        else
            r <= video_gray_out;         
            g <= video_gray_out;         
            b <= video_gray_out;  
        end if;
    else
        r <= "00000000";
        g <= "00000000";
        b <= "00000000";
    end if;
	
end if;
end process;


process(video_start_en_s)
begin
	if (video_start_en_s = '1') then
		led1<='1';
	else
		led1<='0';
	end if;
end process;

end architecture;