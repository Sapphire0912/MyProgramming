library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;

entity video_out_test is
Port (
    ck_ori, rst: in std_logic;
    h_sync, v_sync: out std_logic;
    r, g, b: out std_logic
);
end video_out_test;

architecture Behavioral of video_out_test is
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
    
    constant radius: integer := 50;

    -- Assume Slope = 1
    constant slope: integer := 1;
    
    -- clk
    signal clk_div: std_logic;
    --
    signal h_pol: std_logic := '0';
    signal v_pol: std_logic := '0';

    -- clk divider
    signal freq: std_logic_vector(21 downto 0);
    signal clk_freq: std_logic;

    -- send value
    signal h_left: std_logic_vector(9 downto 0);
    signal cir_o: std_logic_vector(9 downto 0);
    signal tri_x1: std_logic_vector(9 downto 0);
    
begin
    -- clk divider
    process (ck_ori, rst)
    begin
        if (rst = '1') then
            clk_div <= '0';
        elsif (ck_ori 'event and ck_ori = '1') then
            clk_div <= not clk_div;
        end if;
    end process;

    process (ck_ori, rst)
    begin
        if (rst = '1') then
            freq <= (others => '0');
        elsif (ck_ori 'event and ck_ori = '1') then
                freq <= freq + 1;
        end if;
        clk_freq <= freq(20);
    end process;
    
    process (clk_div, rst)
        -- horizontal/vertical counter
        variable h_count: integer range 0 to HT - 1 := 0;
        variable v_count: integer range 0 to VT - 1 := 0;

        -- Dynamic Rectangle
        variable h_rect_left: integer  := 0;
        variable v_rect_upper: integer := 0;
        variable v_rect_lower: integer := 80;
                        
         -- Dynamic Circle
        variable ox: integer := 50;
        variable oy: integer := 200;
        -- Draw Circle(point to center distance)
        variable rx, ry: integer;
                        
        -- Dynamic Triangle
        variable bottom_x1: integer := 0;
        variable bottom_x2: integer := 100;
        variable high_y1: integer := 400;
        variable high_y2: integer := 500;


    begin
        if (rst = '1') then
            h_count := 0;
            v_count := 0;
            h_sync <= not h_pol;
            v_sync <= not v_pol;

        elsif (clk_div 'event and clk_div = '1') then
            -- counters
            if (h_count < HT - 1) then
                h_count := h_count + 1;
            else
                h_count := 0;
                if (v_count < VT - 1) then
                    v_count := v_count + 1;
                else
                    v_count := 0;
                end if;
            end if ;

            -- horizontal sync
            if (h_count < HD + HF or h_count >= HD + HF + HS) then
                h_sync <= not h_pol;
            else
                h_sync <= h_pol;
            end if;

            -- vertical sync 
            if (v_count < VD + VF or v_count >= VD + VF + VS) then
                v_sync <= not v_pol;
            else
                v_sync <= v_pol;
            end if;
        end if;
    
        h_rect_left := conv_integer(h_left);
        ox := conv_integer(cir_o);
        rx := h_count - ox;
        ry := v_count - oy;
        bottom_x1 := conv_integer(tri_x1);

        -- -- Rectangle
        if (h_count > h_rect_left and h_count <= h_rect_left + 80 and v_count > v_rect_upper and v_count <= v_rect_lower) then
            r <= '1';
            g <= '1';
            b <= '1';

        -- -- Circle
        elsif (rx * rx + ry * ry <= radius * radius) then
            r <= '1';
            g <= '1';
            b <= '0';

        -- -- Triangle
        elsif (h_count > bottom_x1 and h_count <= bottom_x1 + 100 and v_count > high_y1 and v_count <= high_y2) then
            -- assume m = i/j then i(x-x1) + j(y1-y) = 0;
            if (h_count + high_y1 - v_count - bottom_x1 > 0) then
                r <= '0';
                g <= '0';
                b <= '1';
            end if;
        else
            r <= '0';
            g <= '0';
            b <= '0';
        end if;
    end process;

    process (clk_freq, rst)
        -- state 0 positive, 1 negative
        variable rect_left: integer := 0;
        variable rect_state: integer := 0;
        variable circle_o: integer := 50;
        variable circle_state: integer := 0;
        variable triangle_x1: integer := 0;
        variable triangle_state: integer := 0;
    begin
        if (rst = '1') then
            rect_left := 0;
            circle_o := 50;
            triangle_x1 := 0;
            rect_state := 0;
            circle_state := 0;
            triangle_state := 0;

        elsif (clk_freq 'event and clk_freq = '1') then
            if (rect_left + 80 > 799) then
                rect_state := 1;
            elsif (rect_left <= 0) then
                rect_state := 0;
            end if;

            if (circle_o + 50 > 799) then
                circle_state := 1;
            elsif (circle_o <= 50) then
                circle_state := 0;
            end if;

            if (triangle_x1 + 100 > 799) then
                triangle_state := 1;
            elsif (triangle_x1 <= 0) then
                triangle_state := 0;
            end if;

            if (rect_state = 0) then
                rect_left := rect_left + 1;
            else
                rect_left := rect_left - 1;
            end if;
            
            if (circle_state = 0) then
                circle_o := circle_o + 1;
            else
                circle_o := circle_o - 1;
            end if;

            if (triangle_state = 0) then
                triangle_x1 := triangle_x1 + 1;
            else
                triangle_x1 := triangle_x1 - 1;
            end if;

        end if;
        h_left <= conv_std_logic_vector(rect_left, 10);
        cir_o <= conv_std_logic_vector(circle_o, 10);
        tri_x1 <= conv_std_logic_vector(triangle_x1, 10);
    end process;

end Behavioral;
