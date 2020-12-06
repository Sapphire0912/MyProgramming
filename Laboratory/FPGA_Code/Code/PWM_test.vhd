library ieee;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_1164.all;

entity PWM_test is
end entity;

architecture Behavioral of PWM_test is
    component PWM
    port(
        clk, reset: in std_logic;
        pwmout: out std_logic;
        count1, count2: out std_logic_vector(3 downto 0)
    );
    end component;

    -- I/P signal
    signal clk: std_logic := '0';
    signal reset: std_logic := '0';
    -- O/P signal
    signal pwmout: std_logic;
    signal count1, count2: std_logic_vector(3 downto 0);

    -- define time period
    constant clk_period: time := 20ns;

begin
    dut: PWM port map(
        clk => clk, reset => reset, pwmout => pwmout,
        count1 => count1, count2 => count2
    );

    clk_gen: process
    begin
        clk <= '0';
        wait for clk_period / 2;
        clk <= '1';
        wait for clk_period / 2;
    end process;

    tb: process
    begin
        wait for 30 ns;
        reset <= '1';
        wait for 15 ns;
        reset <= '0';
        wait;
    end process;

end Behavioral;