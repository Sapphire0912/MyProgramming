library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.all;
use ieee.std_logic_arith.all;

entity Video_IN is
Port ( 
    clk, reset : in std_logic;
    hsync, vsync, comp_sync : out std_logic;
    video_on, p_tick : out std_logic;
    pixel_x, pixel_y : out std_logic_vector(9 downto 0)
);
end Video_IN;

-- assume using 800x600
architecture Behavioral of Video_IN is
    constant HD: integer := 800; -- horizontal display
    constant HF: integer := 56; -- horizontal front porch
    constant HB: integer := 64; -- horizontal back porch
    constant HS: integer := 120; -- horizontal sync pulse
    constant HT: integer := HD + HF + HS + HB -- horizontal total time

    constant VD: integer := 600; -- vertical display
    constant VF: integer := 37; -- vertical front porch
    constant VB: integer := 23; -- vertical back porch
    constant VS: integer := 6; -- vertical sync pulse
    constant VT: integer := VD + VF + VS + VB -- vertical total time

    -- ck divider
    signal clk_div_reg, clk_div_next: unsigned(1 downto 0);

    -- sync counters
    signal vcnt_reg, vcnt_next: unsigned(9 downto 0);
    signal hcnt_reg, hcnt_next: unsigned(9 downto 0);

    -- output buffers
    signal vsync_reg, hsync_reg: std_logic;
    signal vsync_next, hsync_next: std_logic;
    signal hsync_regdelay1, hsync_regdelay2: std_logic;
    signal hsync_nextdelay1, hsync_nextdelay2: std_logic;
    signal vsync_regdelay1, vsync_regdelay2: std_logic;
    signal vsync_nextdelay1, vsync_nextdelay2: std_logic;

    -- status signal
    signal h_end, v_end, pixel_tick: std_logic;
    -- ===

    begin
        process(clk, reset)
        begin
            if (reset = '1') then
                clk_div_reg <= to_unsigned(0, 2);
                vcnt_reg <= (others => '0');
                hcnt_reg <= (others => '0'); 
                vsync_reg <= '0';
                hsync_reg <= '0';
                vsync_regdelay1 <= '0';
                hsync_regdelay1 <= '0';
                vsync_regdelay2 <= '0';
                hsync_regdelay2 <= '0';
            elsif (clk 'event and clk = '1') then
                clk_div_reg <= clk_div_next;
                vcnt_reg <= vcnt_next;
                hcnt_reg <= hcnt_next;
                vsync_reg <= vsync_next;
                hsync_reg <= hsync_next;
            -- Add to cycles of delay for DAC pipeline.
                -- vsync_regdelay1 <= vsync_nextdelay1;
                -- hsync_regdelay1 <= hsync_nextdelay1;
                -- vsync_regdelay2 <= vsync_nextdelay2;
                -- hsync_regdelay2 <= hsync_nextdelay2;
            -- Pipeline registers
                -- vsync_nextdelay1 <= vsync_reg;
                -- hsync_nextdelay1 <= hsync_reg;
                -- vsync_nextdelay2 <= vsync_regdelay1;
                -- hsync_nextdelay2 <= hsync_regdelay1;
            end if;
        end process;

    -- generate a 50MHz enable tick from 100 MHz clock
        clk_div_next <= clk_div_reg + 1;
        pixel_tick <= '1' when clk_div_reg = to_unsigned(1, 2) else '0';
    
    -- h_end and v_end depend on constants above
        h_end <= '1' when hcnt_reg = (HT - 1) else '0';
        v_end <= '1' when vcnt_reg = (VT - 1) else '0';
    
    -- mod-800 horz sync cnter for 640 pixels
        process (hcnt_reg, h_end, pixel_tick)
        begin
            if (pixel_tick = '1') then
                if (h_end = '1') then
                    hcnt_next <= (others => '0');
                else
                    hcnt_next <= hcnt_reg + 1;
                end if;
            else
                hcnt_next <= hcnt_reg;
            end if;
        end process;

    -- mod-525 vertical sync cnter for 480 pixels
        process (vcnt_reg, h_end, v_end, pixel_tick)
        begin
            if (pixel_tick = '1' and h_end = '1') then
                if (v_end = '1') then
                    vcnt_next <= (others => '0');
                else
                    vcnt_next <= vcnt_reg + 1;
                end if;
            else
                vcnt_next <= vcnt_reg;
            end if;
        end process;
    
    -- horz and vert sync, buffered to avoid glitch
        hsync_next <= '1' when (hcnt_reg >= (HD + HF)) and (hcnt_reg <= (HD + HF + HS - 1)) else '0';
        vsync_next <= '1' when (vcnt_reg >= (VD + VF)) and (vcnt_reg <= (VD + VF + VS - 1)) else '0';

    -- video on/off (800)
        video_on <= '1' when (hcnt_reg < HD) and (vcnt_reg < VD) else '0';
    
    -- output signals
        hsync <= hsync_regdelay2;
        vsync <= vsync_regdelay2;
        pixel_x <= std_logic_vector(hcnt_reg);
        pixel_y <= std_logic_vector(vcnt_reg);
        p_tick <= pixel_tick;
    
    -- comp sync signal generation
        comp_sync <= hsync_reg xor vsync_reg;

end Behavioral;
