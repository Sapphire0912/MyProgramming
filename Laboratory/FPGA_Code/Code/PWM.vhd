library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

entity PWM is
    port(
        clk, reset: in std_logic;
        pwmout: out std_logic;
        count1, count2: out std_logic_vector(3 downto 0)
    );
end entity;

architecture Behavioral of PWM is
    -- ctrl state
    signal state: std_logic := '0';

    -- count(4 bit)
    signal cnt1: std_logic_vector(3 downto 0);
    signal cnt2: std_logic_vector(3 downto 0);

begin
    FSM: process (clk, reset, state, cnt1, cnt2)
    begin
        if (reset = '1') then
            state <= '0';
        elsif (clk 'event and clk = '1') then
            case state is
                when '0' =>
                    if (cnt1 = "1001") then
                        state <= '1';
                    end if;
                
                when '1' =>
                    if (cnt2 = "0000") then
                        state <= '0';
                    end if;
                
                when others =>
                    null;
            end case;
        end if;
    end process;

    counter1: process (clk, reset, state, cnt1)
    begin
        if (reset = '1') then
            cnt1 <= "0000";
        elsif (clk 'event and clk = '1') then
            if (state = '0') then
                if (cnt1 = "1001") then
                    cnt1 <= "0000";
                else
                    cnt1 <= cnt1 + 1;
                end if;
            else
                cnt1 <= "0000";
            end if;
        end if;
        count1 <= cnt1;
    end process;

    counter2: process (clk, reset, state, cnt2)
    begin
        if (reset = '1') then
            cnt2 <= "1001";
        elsif (clk 'event and clk = '1') then
            if (state = '1') then
                if (cnt2 = "0000") then
                    cnt2 <= "1001";
                else
                    cnt2 <= cnt2 - 1;
                end if;
            else
                cnt2 <= "1001";
            end if;
        end if;
        count2 <= cnt2;
    end process;

    pwm: process (clk, reset, state)
    begin
        if (reset = '1') then
            pwmout <= '1';
        end if;
        pwmout <= not state;
    end process;

end Behavioral;