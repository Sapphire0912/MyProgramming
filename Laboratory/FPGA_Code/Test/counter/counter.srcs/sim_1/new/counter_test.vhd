-- upper/lower counter_test
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;

entity counter_test is
end counter_test;

architecture Behavioral of counter_test is
    component counter
    port(
        clk: in std_logic;
        reset: in std_logic;
        dout: out std_logic_vector(3 downto 0)
    );
    end component;

    -- I/P signal
    signal clk: std_logic := '0';
    signal reset: std_logic := '0';
    -- O/P signal
    signal dout: std_logic_vector(3 downto 0);

    -- define time period
    constant clk_period: time := 20ns;

begin 
    dut: counter port map(
        clk => clk,
        reset => reset,
        dout => dout
    );
    clk_gen:process
    begin
        clk <= '1';
        wait for clk_period / 2;
        clk <= '0';
        wait for clk_period / 2;
    end process;

    tb:process
    begin
        wait for 20 ns;
        reset <= '1';
        wait for 20 ns;
        reset <= '0';
        wait for 200 ns;
        wait;
    end process;
end Behavioral;
 

-- self-define counter_test
-- library ieee;
-- use ieee.std_logic_1164.all;
-- use ieee.std_logic_unsigned.all;
-- use ieee.std_logic_arith.all;

-- entity counter_test is
-- end counter_test;

-- architecture Behavioral of counter_test is
--     component counter
--     port(
--         clk: in std_logic;
--         reset: in std_logic;
--         upout: out std_logic_vector(4 downto 0);
--         lowout: out std_logic_vector(4 downto 0)
--     );
--     end component;

--     -- I/P signal
--     signal clk: std_logic := '0';
--     signal reset: std_logic := '0';

--     -- O/P signal
--     signal upout: std_logic_vector(4 downto 0);
--     signal lowout: std_logic_vector(4 downto 0);

--     -- define time period
--     constant clk_period: time := 20ns;

-- begin 
--     dut: counter port map(
--         clk => clk,
--         reset => reset,
--         upout => upout,
--         lowout => lowout
--     );
--     clk_gen:process
--     begin
--         clk <= '1';
--         wait for clk_period / 2;
--         clk <= '0';
--         wait for clk_period / 2;
--     end process;

--     tb:process
--     begin
--         wait for 20 ns;
--         reset <= '1';
--         wait for 20 ns;
--         reset <= '0';
--         wait for 200 ns;
--         wait;
--     end process;
-- end Behavioral;
 
