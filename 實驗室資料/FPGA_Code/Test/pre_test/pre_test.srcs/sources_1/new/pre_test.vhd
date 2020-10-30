library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.std_logic_unsigned.all;
use IEEE.std_logic_arith.all;

entity pre_test is
Port (
    ck : in std_logic;
    sw : in std_logic;
    reset : in std_logic;
   ledreg: out std_logic
);
end pre_test;

architecture Behavioral of pre_test is
begin
    process(ck, sw, reset)
    begin
        if reset = '1' then
            ledreg <= '0';
        elsif sw = '0' and rising_edge(ck) then
            ledreg <= '1';
        end if;
    end process;
end Behavioral;
