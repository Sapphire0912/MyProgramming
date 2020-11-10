library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;

entity video_out_test is
Port ( 
    clk_ori, reset: in std_logic;
    hsync, vsync: out std_logic;
    Rout, Gout, Bout: out std_logic
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
    constant h_rect_left: integer := 100;
    constant h_rect_right: integer := 200;
    constant v_rect_upper: integer := 100;
    constant v_rect_lower: integer := 200;
    
    -- Draw Circle(Center Coordinate)
    constant ox: integer := 100;
    constant oy: integer := 400;
    constant radius: integer := 50;

    -- Draw Right Triangle(3 point)
    constant bottom_x1: integer := 300;
    constant bottom_x2: integer := 400;
    constant high_y1: integer := 225;
    constant high_y2: integer := 300;

    constant dx: integer := bottom_x2 - bottom_x1;
    constant dy: integer := high_y2 - high_y1;

    constant A: integer := dx * dy;
    
    -- clk
    signal clk_div: std_logic;
    --
    signal h_pol: std_logic := '0';
    signal v_pol: std_logic := '0';
    
begin
    -- clk divider
    process (clk_ori, reset)
    begin
        if (reset = '1') then
            clk_div <= '0';
        elsif (clk_ori 'event and clk_ori = '1') then
            clk_div <= not clk_div;
        end if;
    end process;

    process (clk_div, reset)
        -- horizontal/vertical counter
        variable h_count: integer range 0 to HT - 1 := 0;
        variable v_count: integer range 0 to VT - 1 := 0;
        
        -- Draw Circle(point to center distance)
        variable rx, ry: integer;

        -- Draw Triangle
        variable area, a, b, c: integer;
        
    begin
        if (reset = '1') then
            h_count := 0;
            v_count := 0;
            hsync <= not h_pol;
            vsync <= not v_pol;
            Rout <= '0';
            Gout <= '0';
            Bout <= '0';
            
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
                hsync <= not h_pol;
            else
                hsync <= h_pol;
            end if;

            -- vertical sync 
            if (v_count < VD + VF or v_count >= VD + VF + VS) then
                vsync <= not v_pol;
            else
                vsync <= v_pol;
            end if;
            
            rx := h_count - ox;
            ry := v_count - oy;
            

            -- Rectangle
            if (h_count > h_rect_left and h_count <= h_rect_right and v_count > v_rect_upper and v_count <= v_rect_lower) then
                Rout <= '1';
                Gout <= '1';
                Bout <= '1';
            -- Circle
            elsif (rx * rx + ry * ry <= radius * radius) then
                Rout <= '1';
                Gout <= '1';
                Bout <= '0';
            -- Triangle
            elsif (h_count > bottom_x1 and h_count <= bottom_x2 and v_count > high_y1 and v_count <= high_y2) then
                    Rout <= '0';
                    Gout <= '1';
                    Bout <= '1';
               
            else
                Rout <= '0';
                Gout <= '0';
                Bout <= '0';
            end if;
            
        end if;
    end process;
end Behavioral;
