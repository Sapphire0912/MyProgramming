library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

entity ball is
    Port(
        clk_ori, reset: in std_logic;
        start: in std_logic;
        left_up, left_down, right_up, right_down: in std_logic;
        hsync, vsync: out std_logic;
        r, g, b: out std_logic
    );
end ball;

architecture Behavioral of ball is
    -- horizontal timing
    constant HD: integer := 800;
    constant HF: integer := 56;
    constant HB: integer := 64;
    constant HS: integer := 120;
    constant HT: integer := HD + HF + HB + HS;
    
    -- vertical timing
    constant VD: integer := 600;
    constant VF: integer := 37;
    constant VB: integer := 23;
    constant VS: integer := 6;
    constant VT: integer := VD + VF + VB + VS;

    -- scanning value
    signal h_pol: std_logic := '0';
    signal v_pol: std_logic := '0';

    -- clk divider
    signal freq: std_logic_vector(21 downto 0);
    signal clk_sync, clk_ball, clk_board: std_logic;

    -- ball size
    constant radius: integer := 60;
    -- ball direction
    signal direction: std_logic := '0';

    -- left/right board horizontal
    constant left_x1: integer := 25;
    constant left_x2: integer := 40;
    constant right_x1: integer := 755;
    constant right_x2: integer := 770;
    constant board_length: integer := 150;
    
    -- send value
    signal ball_ox: std_logic_vector(9 downto 0);
    signal ball_oy: std_logic_vector(9 downto 0);
    signal board_left: std_logic_vector(9 downto 0);
    signal board_right: std_logic_vector(9 downto 0);
    


begin
    -- clk divider
    process (clk_ori, reset)
    begin
        if (reset = '1') then
            freq <= (others => '0');
        elsif (clk_ori 'event and clk_ori = '1') then
            freq <= freq + 1;
        end if;
        clk_sync <= freq(0);
        clk_ball <= freq(19);
    end process;

    -- sync
    process (clk_sync, reset)
        -- horizontal/vertical counter
        variable hcount: integer range 0 to HT - 1:= 0;
        variable vcount: integer range 0 to VT - 1:= 0;

        -- receive ball coordinate
        variable ox, oy: integer;
        -- point to center distance
        variable rx, ry: integer;

        -- receive board coordinate
        variable left, right: integer;

    begin
        if (reset = '1') then
            hcount := 0;
            vcount := 0;
            hsync <= not h_pol;
            vsync <= not v_pol;
        elsif (clk_sync 'event and clk_sync = '1') then
            -- counters
            if (hcount < HT - 1) then
                hcount := hcount + 1;
            else
                hcount := 0;
                if (vcount < VT - 1) then
                    vcount := vcount + 1;
                else
                    vcount := 0;
                end if;
            end if;

            -- horizontal sync
            if (hcount < HD + HF or hcount >= HD + HF + HS) then
                hsync <= not h_pol;
            else
                hsync <= h_pol;
            end if;

            -- vertical sync
            if (vcount < VD + VF or vcount >= VD + VF + VS) then
                vsync <= not v_pol;
            else
                vsync <= v_pol;
            end if;
        end if;

        ox := conv_integer(ball_ox);
        oy := conv_integer(ball_oy);
        rx := hcount - ox;
        ry := vcount - oy;
        left := conv_integer(board_left);
        right := conv_integer(board_right);

        -- display left board
        if (hcount > left_x1 and hcount <= left_x2 and vcount > left and vcount <= left + board_length) then
            r <= '0';
            g <= '1';
            b <= '0';
        -- display right board
        elsif (hcount > right_x1 and hcount <= right_x2 and vcount > right and vcount <= right + board_length) then
            r <= '0';
            g <= '0';
            b <= '1';
        -- display ball
        elsif (rx * rx + ry * ry <= radius * radius) then
            r <= '1';
            g <= '1';
            b <= '0';
        else
            r <= '0';
            g <= '0';
            b <= '0';
        end if;
    end process;

    process (clk_ball, reset, start, left_up, left_down, right_up, right_down)
        -- ball initial coordinate
        variable ball_x: integer := 400;
        variable ball_y: integer := 300;
        -- state: 0 stop, 1 positive, 2 negative 
        variable ball_state: integer := 0;

        -- left/right board vertical
        variable left_y1: integer := 225;
        variable right_y1: integer := 225;
        -- state: 0 stpo, 1 upper, 2 down
        variable left_state: integer := 0;
        variable right_state: integer := 0;

    begin
        if (reset = '1') then
            ball_x := 400;
            ball_y := 300;
            ball_state := 0;

            left_y1 := 225;
            right_y1 := 225;
            left_state := 0;
            right_state := 0;
            if (start = '1') then
                ball_state := (conv_integer(not direction)) + 1;
            end if;
        
        elsif (clk_ball 'event and clk_ball = '1') then
            -- Determine if the ball hits the boundary or the board
            if ((ball_x + radius > right_x1 and ball_y + radius <= right_y1 + 150) or ball_y + radius > 599) then
                ball_state := 2;
            elsif ((ball_x + radius <= left_x2 and ball_y + radius <= left_y1 + 150) or ball_y + radius <= 0) then
                ball_state := 1;
            end if;
            
            -- ball move
            if (ball_state = 1) then
                ball_x := ball_x + 1;
                ball_y := ball_y + 1;
            elsif (ball_state = 2) then
                ball_x := ball_x - 1;
                ball_y := ball_y - 1;
            end if;

            -- Determine whether the board exceeds the boundary
            if (left_up = '1' and left_y1 - board_length > 0) then
                left_state := 1;
            elsif (left_down = '1' and left_y1 + board_length < 600) then
                left_state := 2;
            end if;

            if (right_up = '1' and right_y1 - board_length > 0) then
                right_state := 1;
            elsif (right_down = '1' and right_y1 + board_length < 600) then
                right_state := 2;
            end if;

            -- board move
            if (left_state = 1) then
                left_y1 := left_y1 + 3;
            elsif (left_state = 2) then
                left_y1 := left_y1 - 3;
            end if;

            if (right_state = 1) then
                right_y1 := right_y1 + 3;
            elsif (right_state = 2) then
                right_y1 := right_y1 - 3;
            end if;

        end if;

        ball_ox <= conv_std_logic_vector(ball_x, 10);
        ball_oy <= conv_std_logic_vector(ball_y, 10);
        board_left <= conv_std_logic_vector(left_y1, 10);
        board_right <= conv_std_logic_vector(right_y1, 10);

    end process;

end Behavioral;
