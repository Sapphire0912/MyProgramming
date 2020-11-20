----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    16:06:38 09/29/2016 
-- Design Name: 
-- Module Name:    video_in - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------



library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity video_in is

    port(
        clk : in std_logic;    
        rst : in  std_logic;
        video_data : in std_logic_vector(7 downto 0);
        video_start_en : out std_logic ;
        cnt_video_hsync : out integer range 0 to 1715
    );
end video_in;

architecture Behavioral of video_in is
--抓sav----------------------------
signal video_sav_state : std_logic_vector(1 downto 0);


signal video_F_en: std_logic; 
signal video_V_en: std_logic;
signal sav_temp: std_logic_vector(7 downto 0);

--影像訊號-----------------
signal video_start_en_s  : std_logic ;
signal cnt_video_hsync_s : integer range 0 to 1715;

begin

--內部訊號接到外部----
video_start_en  <= video_start_en_s;
cnt_video_hsync <= cnt_video_hsync_s;
---------------------

video_state : process(clk , rst , video_data,video_sav_state)
begin
if rst = '0' then
    video_sav_state <= "00";
elsif clk'event and clk = '1' then    
    case video_sav_state is
        when "00"  => 
            if video_data = x"ff" then                
                video_sav_state <="01";
            else
                video_sav_state <="00";
            end if;
        when "01"  =>
            if video_data = x"00" then
                video_sav_state <="10";
            else
                video_sav_state <="00";
            end if;
        when "10"  =>
            if video_data = x"00" then
                video_sav_state <="11";
            else
                video_sav_state <="00";
            end if;
        when "11"  =>
            video_sav_state <="00";            
        when others => null;    
    end case;
end if;
end process;

first_pixel : process(clk , rst , video_data,video_F_en,video_V_en,sav_temp,video_start_en_s)
begin
if rst = '0' then
    video_start_en_s <= '0';
    video_F_en <= '0';
    video_V_en <= '0';
    sav_temp <= "XXXXXXXX";
elsif clk'event and clk = '1' then
    case video_sav_state is
        when "11"  => 
            sav_temp <= video_data;
            if video_data(4) = '0' and sav_temp(4) = '1' and video_V_en = '1' and video_F_en = '1' then 
                video_start_en_s <= '1';
            elsif video_data(5) = '0' and sav_temp(5) = '1' and video_F_en = '1' then 
                video_V_en <= '1';
            elsif video_data(6) = '1' and sav_temp(6) = '0' then 
                video_F_en <= '1';
            end if;    
        when others => null;
    end case;
end if;
end process;

video_cnt : process(rst, clk,video_start_en_s,cnt_video_hsync_s)
begin
if rst = '0' then
    cnt_video_hsync_s <= 0;
else
    if clk'event and clk = '1' then
        if video_start_en_s = '1' then
            if cnt_video_hsync_s = 1715 then
                cnt_video_hsync_s <= 0;
            else
                cnt_video_hsync_s <= cnt_video_hsync_s + 1;
            end if;
        else
            cnt_video_hsync_s <= 0;
        end if;
    end if;
end if;
end process;
end Behavioral;

