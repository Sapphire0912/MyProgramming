library ieee
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

entity vga_rgb_test is
    port(
        clk_ori, reset: in std_logic;
        hsync, vsync: out std_logic;

        horizontal, vertical: out std_logic_vector(9 downto 0);
        Rout, Gout, Bout, H, V: out std_logic
    );
end entity;

architecture rgb of vga_rgb_test is
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

    -- clk
    signal clk_div: std_logic;

    -- horizontal/vertical signal value
    signal h_pol: std_logic := '0';
    signal v_pol: std_logic := '0';

-- =========================================================
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
        -- set horizontal/vertical range -> define 0
        variable h_count: integer range 0 to HT - 1 := 0;
        variable v_count: integer range 0 to VT - 1 := 0;
    begin
        if (reset = '1') then
            h_count := 0;
            v_count := 0;
            hsync <= not h_pol;
            vsync <= not v_pol;
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

            -- horizontal signal value
            if (h_count < HD + HF or h_count >= HD + HF + HS) then
                hsync <= not h_pol;
            else
                hsync <= h_pol;
            end if;

            -- vertical signal value
            if (v_count < VD + VF or v_count >= VD + VF + VS) then
                vsync <= not v_pol;
            else
                vsync <= v_pol;
            end if;
        end if;


        
    end process;

end architecture;