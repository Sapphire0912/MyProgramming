----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    14:30:03 09/30/2016 
-- Design Name: 
-- Module Name:    i2c - Behavioral 
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

entity i2c is
   port(clk : in  std_logic;                   
        rst : in  std_logic;
        sda : inout std_logic;
        scl : inout std_logic
    );
end i2c;

architecture Behavioral of i2c is

type STATE_I2C is (start, slv_ack, wr , stop); 
signal I2C_state : STATE_I2C ;
constant I2C_device_address_1 : std_logic_vector(7 downto 0):= "10111010";--0xba
constant I2C_device_address_2 : std_logic_vector(7 downto 0):= "10111000";--0xb8
constant I2C_word_address : std_logic_vector(7 downto 0):= "00000011";
constant I2C_write_data : std_logic_vector(7 downto 0):= "00001001";
signal I2C_bit_cnt : integer range 0 to 8;
signal I2C_data_state : integer range 0 to 2 ;
signal divcount : std_logic_vector(18 downto 0);
signal data_number :std_logic:='0';

begin

process(clk, rst, scl, sda, I2C_bit_cnt, divcount,I2C_state)
begin
if rst = '0' then
    I2C_state <= start;
    data_number<='0';
elsif clk'event and clk = '1' then
    case I2C_state is 
        when start => 
            if scl = '0' and sda = '0' then
                I2C_state <= wr ;
                end if;                
        when wr => 
            if I2C_bit_cnt = 8 and divcount(17 downto 0) = "010000000000000000" then 
                I2C_state <= slv_ack;
                end if;                
        when slv_ack => 
            if I2C_bit_cnt = 0 and divcount(17 downto 0) = "010000000000000000"  then
                    if I2C_data_state < 2 then
                    I2C_state <= wr ;                      
                    else 
                        I2C_state <= stop;
                    end if;
                end if;
        when stop=>
            if data_number < '1' and divcount(17 downto 0) = "111000000000000000"  then  
                data_number<='1';
                I2C_state <= start ;
            end if;         
        when others => null;
     end case ;
end if;
end process;

process(clk, rst, divcount,scl)
begin
if rst = '0' then
    scl <= '1';
elsif clk'event and clk = '1' then
    case I2C_state is 
        when start => 
            if divcount(18) = '1' then
                scl <= '0';
            end if;
        when stop =>  
            if  divcount(17) = '1' then
                scl <= '1' ;
            end if;
        when others => 
            scl <= divcount(17) ;
    end case ;
end if;
end process;

process(clk, rst, scl, I2C_data_state, divcount,sda)
begin
if rst = '0' then
    sda <= '1' ;
elsif clk'event and clk = '1' then
    case I2C_state is 
        when start =>
            if divcount(17) = '1' then
                sda <= '0';
            end if;
        when wr => 
            if data_number ='0' and divcount(17 downto 0) = "010000000000000001" then                     
                if I2C_data_state = 0 then
                    sda <= I2C_device_address_1(7 - I2C_bit_cnt);
                elsif I2C_data_state = 1 then
                    sda <= I2C_word_address(7 - I2C_bit_cnt);
                else
                    sda <= I2C_write_data(7 - I2C_bit_cnt);
                end if;
            elsif data_number ='1' and divcount(17 downto 0) = "010000000000000001" then                     
                if I2C_data_state = 0 then
                    sda <= I2C_device_address_2(7 - I2C_bit_cnt);
                elsif I2C_data_state = 1 then
                    sda <= I2C_word_address(7 - I2C_bit_cnt);
                else
                    sda <= I2C_write_data(7 - I2C_bit_cnt);
                end if;
            end if;
        when slv_ack =>
            sda <= 'Z';
            
        when stop =>
            if scl = '1' then
                if divcount(17 downto 0) = "110000000000000000" then
                    sda <= '1';                
                end if;                
            else
                sda <= '0';
            end if;
        when others => null;
    end case ;
end if;
end process;

process(clk, rst, divcount, I2C_bit_cnt,I2C_data_state)
begin
if rst = '0' then
   I2C_data_state <= 0;
elsif clk'event and clk = '1' then
    case I2C_state is
        when slv_ack =>
            if I2C_bit_cnt = 0 and divcount(17 downto 0) = "010000000000000000"  then
                I2C_data_state <= I2C_data_state + 1;
            end if;
        when stop=>
            I2C_data_state<=0;
        when others => null;
    end case;  
end if;
end process;

process(clk, rst, divcount,I2C_bit_cnt)
begin
if rst = '0' then
    I2C_bit_cnt <= 0;
elsif clk'event and clk = '0' then
    if divcount(17 downto 0) = "110000000000000000" then
        case I2C_state is          
            when wr => 
                if I2C_bit_cnt < 8 then                
                    I2C_bit_cnt <= I2C_bit_cnt + 1 ;
                else 
                    I2C_bit_cnt <= 0;
                end if;
            when slv_ack => 
                if I2C_bit_cnt < 1 then                
                    I2C_bit_cnt <= I2C_bit_cnt + 1 ;
                else 
                    I2C_bit_cnt <= 0;
                end if;                            
            when others => null;
        end case ;
    end if;     
end if;
end process;

process(rst , clk) 
begin 
if rst='0' then       
    divcount <= (Others => '0');
elsif clk'event and clk = '1' then
    divcount <= divcount + '1';
end if; 
end process;

end architecture;
