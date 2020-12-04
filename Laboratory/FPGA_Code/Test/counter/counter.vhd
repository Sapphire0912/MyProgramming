library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;

entity counter is
    port(
        clk, reset: in std_logic;
        upout: out std_logic_vector(4 downto 0);
        lowout: out std_logic_vector(4 downto 0)
    );
end entity;

architecture behavior of counter is
    constant upper_limit: integer := 14;
    constant lower_limit: integer := 6;
    
    signal upcount: std_logic_vector(4 downto 0);
    signal lowcount: std_logic_vector(4 downto 0);

begin
    -- upper counter
    process (clk, reset, upcount)
    begin
        if (reset = '1') then
            upcount <= conv_std_logic_vector(lower_limit, 5);
        elsif (clk 'event and clk = '1') then
            if (conv_integer(upcount) < upper_limit) then
                upcount <= upcount + 1;
            else
                upcount <= conv_std_logic_vector(lower_limit, 5);
            end if;
        end if;
        upout <= upcount;
    end process;

    -- lower counter
    process (clk, reset, lowcount)
    begin
        if (reset = '1') then
            lowcount <= conv_std_logic_vector(upper_limit, 5);
        elsif (clk 'event and clk = '1') then
            if (conv_integer(lowcount) > lower_limit) then
                lowcount <= lowcount - 1;
            else
                lowcount <= conv_std_logic_vector(upper_limit, 5);
            end if;
        end if;
        lowout <= lowcount;
    end process;

end behavior;

-- upper counter
-- library ieee;  
-- use ieee.std_logic_1164.all;  
-- use ieee.std_logic_unsigned.all;  
-- use ieee.std_logic_unsigned.all;  
  
-- entity counter is  
--     port(  
--         clk     :in     std_logic;  
--         reset   :in     std_logic;  
--         dout   :out    std_logic_vector(3 downto 0)  
--         );  
-- end entity;  
  
-- architecture Behavioral of counter is  
  
-- signal temp :std_logic_vector(3 downto 0);  
  
-- begin  
--     process(clk,reset)  
--     begin  
--         if (reset = '1') then  
--             temp <= "0000";  
--         elsif (clk 'event and clk = '1') then
--             if (temp = "1001") then
--                 temp <= "0000";
--             else
--                 temp <= temp + 1; 
--             end if; 
--         end if;  
--     end process;  
--     dout <= temp;  
-- end Behavioral;

-- lower counter
-- library ieee;  
-- use ieee.std_logic_1164.all;  
-- use ieee.std_logic_unsigned.all;  
-- use ieee.std_logic_unsigned.all;  
  
-- entity counter is  
--     port(  
--         clk     :in     std_logic;  
--         reset   :in     std_logic;  
--         dout   :out    std_logic_vector(3 downto 0)  
--         );  
-- end entity;  
  
-- architecture Behavioral of counter is  
  
-- signal temp :std_logic_vector(3 downto 0);  
  
-- begin  
--     process(clk,reset)  
--     begin  
--         if (reset = '1') then  
--             temp <= "1001";  
--         elsif (clk 'event and clk = '1') then
--             if (temp = "0000") then
--                 temp <= "1001";
--             else
--                 temp <= temp - 1; 
--             end if; 
--         end if;  
--     end process;  
--     dout <= temp;  
-- end Behavioral;