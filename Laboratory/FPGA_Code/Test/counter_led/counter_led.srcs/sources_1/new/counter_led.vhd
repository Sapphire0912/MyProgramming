library ieee;  
use ieee.std_logic_1164.all;  
use ieee.std_logic_unsigned.all;  
use ieee.std_logic_unsigned.all;  
  
entity counter_led is  
    port(  
        clk, reset: in std_logic;
        ledout: out std_logic_vector(7 downto 0);
        sevenout: out std_logic_vector(6 downto 0)
    );  
end entity;  
  
architecture Behavioral of counter_led is  
    signal count: std_logic_vector(3 downto 0);
    signal freq: std_logic_vector(24 downto 0);
    signal clk_div: std_logic;
begin  
    process (clk, reset)
    begin
        if (reset = '1') then
            freq <= (others => '0');
        elsif (clk 'event and clk = '1') then
            freq <= freq + 1;
        end if;
        clk_div <= freq(24);
    end process;

--    upper counter
    process(clk_div, reset, count)  
    begin  
        if (reset = '1') then  
            count <= "0000";  
        elsif (clk_div 'event and clk_div = '1') then
--            case count is
--                when "0000" => ledout <= "00000000"; 
--                when "0001" => ledout <= "10000000"; 
--                when "0010" => ledout <= "01000000"; 
--                when "0011" => ledout <= "00100000"; 
--                when "0100" => ledout <= "00010000"; 
--                when "0101" => ledout <= "00001000"; 
--                when "0110" => ledout <= "00000100"; 
--                when "0111" => ledout <= "00000010"; 
--                when "1000" => ledout <= "00000001"; 
--                when "1001" => ledout <= "10000001"; 
--                when others => ledout <= "00000000"; 
--            end case;
        
            case count is
                when "0000" => sevenout <= "0111111";
                when "0001" => sevenout <= "0000110";
                when "0010" => sevenout <= "1011011";
                when "0011" => sevenout <= "1001111";
                when "0100" => sevenout <= "1100110";
                when "0101" => sevenout <= "1101101";
                when "0110" => sevenout <= "1111101";
                when "0111" => sevenout <= "0000111";
                when "1000" => sevenout <= "1111111";
                when "1001" => sevenout <= "1101111";
                when others => sevenout <= "0000000";
            end case;

            if (count = "1001") then
                count <= "0000";
            else
                count <= count + 1; 
            end if;
        end if;
    end process;

    -- lower counter
    -- process(clk_div, reset, count)  
    -- begin  
    --     if (reset = '1') then  
    --         count <= "1001";  
    --     elsif (clk_div 'event and clk_div = '1') then
    --         case count is
    --             when "0000" => ledout <= "00000000";
    --             when "0001" => ledout <= "10000000";
    --             when "0010" => ledout <= "01000000";
    --             when "0011" => ledout <= "00100000";
    --             when "0100" => ledout <= "00010000";
    --             when "0101" => ledout <= "00001000";
    --             when "0110" => ledout <= "00000100";
    --             when "0111" => ledout <= "00000010";
    --             when "1000" => ledout <= "00000001";
    --             when "1001" => ledout <= "10000001";
    --             when others => ledout <= "00000000";
    --         end case;
            
    --         if (count = "0000") then
    --             count <= "1001";
    --         else
    --             count <= count - 1; 
    --         end if;
    --     end if;
    -- end process;
    

end Behavioral;