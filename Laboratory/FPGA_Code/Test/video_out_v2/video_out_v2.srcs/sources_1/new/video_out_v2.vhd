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
    
    -- Draw Rectangle(4 point)
    -- constant h_rect_left: integer := 100;
    -- constant h_rect_right: integer := 180;
    -- constant v_rect_upper: integer := 100;
    -- constant v_rect_lower: integer := 180;
    
    -- Draw Circle(Center Coordinate)
    -- constant ox: integer := 100;
    -- constant oy: integer := 400;
    constant radius: integer := 50;

    -- Draw Right Triangle(3 point)
    -- constant bottom_x1: integer := 300;
    -- constant bottom_x2: integer := 400;
    -- constant high_y1: integer := 200;
    -- constant high_y2: integer := 300;

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
            clk_freq <= freq(21);
        end if;
    end process;

    process (clk_div, rst)
        -- horizontal/vertical counter
        variable h_count: integer range 0 to HT - 1 := 0;
        variable v_count: integer range 0 to VT - 1 := 0;
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
    end process;

    process (clk_freq, rst)
        -- Count
        variable h_display: integer range 0 to HD - 1 := 0;
        variable v_display: integer range 0 to VD - 1 := 0;
        -- Dynamic Rectangle
        variable h_rect_left: integer;
        variable h_rect_right: integer;
        variable v_rect_upper: integer;
        variable v_rect_lower: integer;
                
        -- Dynamic Circle
        variable ox: integer;
        variable oy: integer;
        -- Draw Circle(point to center distance)
        variable rx, ry: integer;
                
        -- Dynamic Triangle
        variable bottom_x1: integer;
        variable bottom_x2: integer;
        variable high_y1: integer;
        variable high_y2: integer;
    
    begin
        if(rst = '1') then
            r <= '0';
            g <= '0';
            b <= '0';

            -- initial coordinate
            h_rect_left := 0;
            h_rect_right := 80;
            v_rect_upper := 0;
            v_rect_lower := 80;
            ox := 0;
            oy := 200;
            bottom_x1 := 0;
            bottom_x2 := 100;
            high_y1 := 400;
            high_y2 := 500;

        elsif (clk_freq 'event and clk_freq = '1') then
            rx := h_display - ox;
            ry := v_display - oy;
        
            -- Rectangle
            if (h_display > h_rect_left and h_display <= h_rect_right and v_display > v_rect_upper and v_display <= v_rect_lower) then
                r <= '1';
                g <= '1';
                b <= '1';
            -- Circle
            elsif (rx * rx + ry * ry <= radius * radius) then
                r <= '1';
                g <= '1';
                b <= '0';
            -- Triangle
            elsif (h_display > bottom_x1 and h_display <= bottom_x2 and v_display > high_y1 and v_display <= high_y2) then
                if (h_display + high_y1 - v_display - bottom_x1 = 0) then
                    r <= '0';
                    g <= '0';
                    b <= '1';
                end if;
            else
                r <= '0';
                g <= '0';
                b <= '0';
            end if;
            h_rect_left := h_rect_left + 1;
            h_rect_right := h_rect_right + 1;
            v_rect_upper := v_rect_upper + 1;
            v_rect_lower := v_rect_lower + 1;
            ox := ox + 1;
            oy := oy + 1;
            bottom_x1 := bottom_x1 + 1;
            bottom_x2 := bottom_x2 + 1;
            high_y1 := high_y1 + 1;
            high_y2 := high_y2 +1;
        end if;
    end process;

end Behavioral;
