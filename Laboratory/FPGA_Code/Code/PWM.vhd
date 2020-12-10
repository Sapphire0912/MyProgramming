library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

-- sw: I/P signal; up_ssd, low_ssd: upper/lower seven-segement display
entity PWM is
    port(
        clk, reset: in std_logic;
        sw: in std_logic_vector(7 downto 0);
        pwmout: out std_logic;
        up_ssd, low_ssd: out std_logic_vector(6 downto 0)
    );
end entity;

architecture Behavioral of PWM is
    -- clock divider
    signal freq: std_logic_vector(25 downto 0);
    signal clk_div: std_logic;

    -- receive sw values
    signal bound: std_logic_vector(7 downto 0);

    -- state: 0, upper; 1, lower
    signal state: std_logic;

    -- count 
    signal count1: std_logic_vector(7 downto 0);
    signal count2: std_logic_vector(7 downto 0);

    -- pwm value(state, pwm_value; 0, 1; 1, 0)
    signal pwm_value: std_logic;

begin
    clk_div <= freq(25);
    pwmout <= pwm_value;

    freq_div: process (clk, reset, freq)
    begin
        if (reset = '1') then
            freq <= (others => '0');
        elsif (clk 'event and clk = '1') then
            freq <= freq + '1';
        end if;
    end process;

    set_bound: process (clk_div, reset, sw, bound)
    begin
        if (reset = '1') then
            bound <= (others => '0');
        elsif (clk_div 'event and clk_div = '1') then
            bound <= sw;
        end if;
    end process;

    FSM: process (clk_div, reset, state, bound, count1, count2)
    begin
        if (reset = '1') then
            state <= '0';
        elsif (clk_div 'event and clk_div = '1') then
            case state is
                when '0' =>
                    if (count1 >= bound - '1') then
                        state <= '1';
                    end if;
                when '1' =>
                    if (count2 <= bound + '1') then
                        state <= '0';
                    end if;
                when others =>
                    null;
            end case;
        end if;
    end process;

    counter1: process (clk_div, reset, state, count1)
    begin
        if (reset = '1') then
            count1 <= (others => '0');
        elsif (clk_div 'event and clk_div = '1') then
            if (state = '0') then
                count1 <= count1 + '1';
            else
                count1 <= (others => '0');  
            end if;
        end if;
    end process;

    counter2: process (clk_div, reset, state, count2)
    begin
        if (reset = '1') then
            count2 <= "00001001";
        elsif (clk_div 'event and clk_div = '1') then
            if (state = '1') then
                count2 <= count2 - '1';
            else        
                count2 <= "00001001";
            end if;
        end if;
    end process;

    pwm: process (clk_div, reset, state, pwm_value)
    begin
        if (reset = '1') then
            pwm_value <= '1';
        elsif (clk_div 'event and clk_div = '1') then
            pwm_value <= not state;
        end if;
    end process;

-------- actual circuit --------
    -- up_ssd(common: positive)
    upper_ssd: process (clk_div, reset, count1) 
    begin
        if (reset = '1') then
            up_ssd <= "0000001";
        elsif (clk_div 'event and clk_div = '1') then
            case count1 is
                when "00000000" =>
                    up_ssd <= "0000001";
                when "00000001" =>
                    up_ssd <= "1001111";
                when "00000010" =>
                    up_ssd <= "0010010";
                when "00000011" =>
                    up_ssd <= "0000110";
                when "00000100" =>
                    up_ssd <= "1001100";
                when "00000101" => 
                    up_ssd <= "0100100";
                when "00000110" =>
                    up_ssd <= "0100000";
                when "00000111" =>
                    up_ssd <= "0001111";
                when "00001000" =>
                    up_ssd <= "0000000";
                when "00001001" =>
                    up_ssd <= "0000100";
                when others => 
                    null;
            end case;
        end if;
    end process;

    -- low_ssd(common: positive)
    lower_ssd: process (clk_div, reset, count2) 
    begin
        if (reset = '1') then
            low_ssd <= "0000100";
        elsif (clk_div 'event and clk_div = '1') then
            case count2 is
                when "00000000" =>
                    low_ssd <= "0000001";
                when "00000001" =>
                    low_ssd <= "1001111";
                when "00000010" =>
                    low_ssd <= "0010010";
                when "00000011" =>
                    low_ssd <= "0000110";
                when "00000100" =>
                    low_ssd <= "1001100";
                when "00000101" => 
                    low_ssd <= "0100100";
                when "00000110" =>
                    low_ssd <= "0100000";
                when "00000111" =>
                    low_ssd <= "0001111";
                when "00001000" =>
                    low_ssd <= "0000000";
                when "00001001" =>
                    low_ssd <= "0000100";
                when others => 
                    null;
            end case;
        end if;
    end process;

end Behavioral;