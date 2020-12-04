library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;

entity led_move is
    Port ( 
        clk_ori, reset: in std_logic;
        pl1, pl2: in std_logic;
        led: out std_logic_vector(0 to 7)
    );
end led_move;

-- 會有按按鈕提早打的問題
architecture Behavioral of led_move is
    -- clk divider
    signal freq: std_logic_vector(25 downto 0);
    signal clk_freq: std_logic;
    
    -- right to serve
    signal serve: std_logic_vector(1 downto 0) := "10";
begin
    -- clk divider
    process (clk_ori, reset)
    begin
        if (reset = '1') then
            freq <= (others => '0');
        elsif (clk_ori 'event and clk_ori = '1') then
            freq <= freq + 1;
        end if;
        clk_freq <= freq(23);
    end process;

    -- led move
    process (clk_freq, reset, pl1, pl2)
        variable ball: integer range 0 to 9 := 1;
        variable start: integer := 0;
        variable score1: integer := 0;
        variable score2: integer := 0;
    begin
        if (reset = '1') then
            -- after: add count score 
            serve <= "10";
            ball := 1;
            start := 0;
            score1 := 0;
            score2 := 0;
        
        elsif (clk_freq 'event and clk_freq = '1') then
            case ball is
                when 1 => led <= "10000000";
                when 2 => led <= "01000000";
                when 3 => led <= "00100000";
                when 4 => led <= "00010000";
                when 5 => led <= "00001000";
                when 6 => led <= "00000100";
                when 7 => led <= "00000010";
                when 8 => led <= "00000001";
                when others => led <= "00000000";
            end case;

            if (serve(1) = '1') then
                if (pl1 = '1' and (ball /= 1 or ball <= 0)) then
                    -- pl1 lose
                    ball := 8;
                    score2 := score2 + 1;
                    serve <= "01";
                else
                    ball := ball + 1;
                end if;
            end if;

            if (serve(0) = '1') then
                if (pl2 = '1' and (ball /= 8 or ball > 8)) then
                    -- pl2 lose
                    ball := 1;
                    score1 := score1 + 1;
                    serve <= "10";
                else
                    ball := ball - 1;
                end if;
            end if;
        end if;
    
    end process;

end Behavioral;
