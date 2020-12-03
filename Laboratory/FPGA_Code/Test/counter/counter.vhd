library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;

entity counter is
    port(
        clk, reset: in std_logic;
        dout: out std_logic_vector(3 downto 0)
    );
end entity;

architecture behavior of counter is
    constant upper_limit: integer := 9;
    constant lower_limit: integer := 0;
    
    signal count: std_logic_vector(3 downto 0);
    signal ctrl: std_logic;
    
begin
    -- upper counter
    process (clk, reset, count)
    begin
        if (reset = '1') then
            count <= conv_std_logic_vector(lower_limit, 4);
            ctrl <= '0';
        elsif (clk 'event and clk = '1') then
            if (ctrl = '0') then
                if (conv_integer(count) < upper_limit) then
                    count <= count + 1;
                else
                    ctrl <= '1';
                end if;
            end if;
        end if;
        dout <= count;
    end process;

    -- lower counter
    process (clk, reset, count)
    begin
        if (reset = '1') then
            count <= conv_std_logic_vector(lower_limit, 4);
            ctrl <= '0';
        elsif (clk 'event and clk = '1') then
            if (ctrl = '1') then
                if (conv_integer(count) > lower_limit) then
                    count <= count - 1;
                else
                    ctrl <= 0;
                end if;
            end if;
        end if;
        dout <= count;
    end process;
end behavior;