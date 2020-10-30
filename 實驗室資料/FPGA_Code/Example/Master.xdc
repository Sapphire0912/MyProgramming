## Clock Source
set_property PACKAGE_PIN Y9 [get_ports {ck}];  # "GCLK"
set_property IOSTANDARD LVCMOS25 [get_ports {ck}];

## HDMI Output
#set_property PACKAGE_PIN Y13 [get_ports {hdmi_data[0]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[0]}]
#set_property PACKAGE_PIN AA13 [get_ports {hdmi_data[1]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[1]}]
#set_property PACKAGE_PIN AA14 [get_ports {hdmi_data[2]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[2]}]
#set_property PACKAGE_PIN Y14 [get_ports {hdmi_data[3]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[3]}]
#set_property PACKAGE_PIN AB15 [get_ports {hdmi_data[4]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[4]}]
#set_property PACKAGE_PIN AB16 [get_ports {hdmi_data[5]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[5]}]
#set_property PACKAGE_PIN AA16 [get_ports {hdmi_data[6]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[6]}]
#set_property PACKAGE_PIN AB17 [get_ports {hdmi_data[7]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[7]}]
#set_property PACKAGE_PIN AA17 [get_ports {hdmi_data[8]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[8]}]
#set_property PACKAGE_PIN Y15 [get_ports {hdmi_data[9]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[9]}]
#set_property PACKAGE_PIN W13 [get_ports {hdmi_data[10]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[10]}]
#set_property PACKAGE_PIN W15 [get_ports {hdmi_data[11]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[11]}]
#set_property PACKAGE_PIN V15 [get_ports {hdmi_data[12]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[12]}]
#set_property PACKAGE_PIN U17 [get_ports {hdmi_data[13]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[13]}]
#set_property PACKAGE_PIN V14 [get_ports {hdmi_data[14]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[14]}]
#set_property PACKAGE_PIN V13 [get_ports {hdmi_data[15]}]
#set_property IOSTANDARD LVCMOS25 [get_ports {hdmi_data[15]}]

#set_property PACKAGE_PIN U16 [get_ports hdmi_data_e]
#set_property IOSTANDARD LVCMOS25 [get_ports hdmi_data_e]
#set_property PACKAGE_PIN V17 [get_ports hdmi_hsync]
#set_property IOSTANDARD LVCMOS25 [get_ports hdmi_hsync]
#set_property PACKAGE_PIN W17 [get_ports hdmi_vsync]
#set_property IOSTANDARD LVCMOS25 [get_ports hdmi_vsync]
#set_property PACKAGE_PIN W18 [get_ports hdmi_clk]
#set_property IOSTANDARD LVCMOS25 [get_ports hdmi_clk]

#set_property PACKAGE_PIN AA18 [get_ports iic_rtl_scl_io]
#set_property IOSTANDARD LVCMOS25 [get_ports iic_rtl_scl_io]

#set_property PACKAGE_PIN Y16 [get_ports iic_rtl_sda_io]
#set_property IOSTANDARD LVCMOS25 [get_ports iic_rtl_sda_io]

## User LEDs
#set_property -dict {PACKAGE_PIN U14 IOSTANDARD LVCMOS25} [get_ports {leds_8bits_tri_o[7]}]
#set_property -dict {PACKAGE_PIN U19 IOSTANDARD LVCMOS25} [get_ports {leds_8bits_tri_o[6]}]
#set_property -dict {PACKAGE_PIN W22 IOSTANDARD LVCMOS25} [get_ports {leds_8bits_tri_o[5]}]
#set_property -dict {PACKAGE_PIN V22 IOSTANDARD LVCMOS25} [get_ports {leds_8bits_tri_o[4]}]
#set_property -dict {PACKAGE_PIN U21 IOSTANDARD LVCMOS25} [get_ports {leds_8bits_tri_o[3]}]
#set_property -dict {PACKAGE_PIN U22 IOSTANDARD LVCMOS25} [get_ports {leds_8bits_tri_o[2]}]
#set_property -dict {PACKAGE_PIN T21 IOSTANDARD LVCMOS25} [get_ports {leds_8bits_tri_o[1]}]
set_property -dict {PACKAGE_PIN T22 IOSTANDARD LVCMOS25} [get_ports {ledreg}]

## User DIP Switches
#set_property -dict {PACKAGE_PIN F22 IOSTANDARD LVCMOS25} [get_ports {sws_8bits_tri_i[0]}]
#set_property -dict {PACKAGE_PIN G22 IOSTANDARD LVCMOS25} [get_ports {sws_8bits_tri_i[1]}]
#set_property -dict {PACKAGE_PIN H22 IOSTANDARD LVCMOS25} [get_ports {sws_8bits_tri_i[2]}]
#set_property -dict {PACKAGE_PIN F21 IOSTANDARD LVCMOS25} [get_ports {sws_8bits_tri_i[3]}]
#set_property -dict {PACKAGE_PIN H19 IOSTANDARD LVCMOS25} [get_ports {sws_8bits_tri_i[4]}]
set_property -dict {PACKAGE_PIN H18 IOSTANDARD LVCMOS25} [get_ports {sw}]
#set_property -dict {PACKAGE_PIN H17 IOSTANDARD LVCMOS25} [get_ports {sws_8bits_tri_i[6]}]
#set_property -dict {PACKAGE_PIN M15 IOSTANDARD LVCMOS25} [get_ports {sws_8bits_tri_i[7]}]

## User Push Buttons
#set_property -dict {PACKAGE_PIN P16 IOSTANDARD LVCMOS25} [get_ports {btns_5bits_tri_i[0]}]
#set_property -dict {PACKAGE_PIN R16 IOSTANDARD LVCMOS25} [get_ports {btns_5bits_tri_i[1]}]
#set_property -dict {PACKAGE_PIN N15 IOSTANDARD LVCMOS25} [get_ports {btns_5bits_tri_i[2]}]
set_property -dict {PACKAGE_PIN R18 IOSTANDARD LVCMOS25} [get_ports {reset}]
#set_property -dict {PACKAGE_PIN T18 IOSTANDARD LVCMOS25} [get_ports {btns_5bits_tri_i[4]}]

## FMC
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[16]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[15]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[14]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[13]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[12]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[11]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[10]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[9]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[8]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[7]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[6]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[5]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[4]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[3]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[2]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[1]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_in_p[0]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[16]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[15]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[14]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[13]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[12]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[11]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[10]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[9]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[8]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[7]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[6]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[5]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[4]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[3]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[2]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[1]}]
#set_property IOSTANDARD LVDS_25 [get_ports {la_out_p[0]}]

## FMC la [0:16]   EES273-J18
#set_property PACKAGE_PIN M19 [get_ports {la_out_p[0]}]
#set_property PACKAGE_PIN N19 [get_ports {la_out_p[1]}]
#set_property PACKAGE_PIN P17 [get_ports {la_out_p[2]}]
#set_property PACKAGE_PIN N22 [get_ports {la_out_p[3]}]
#set_property PACKAGE_PIN M21 [get_ports {la_out_p[4]}]
#set_property PACKAGE_PIN J18 [get_ports {la_out_p[5]}]
#set_property PACKAGE_PIN L21 [get_ports {la_out_p[6]}]
#set_property PACKAGE_PIN T16 [get_ports {la_out_p[7]}]
#set_property PACKAGE_PIN J21 [get_ports {la_out_p[8]}]
#set_property PACKAGE_PIN R20 [get_ports {la_out_p[9]}]
#set_property PACKAGE_PIN R19 [get_ports {la_out_p[10]}]
#set_property PACKAGE_PIN N17 [get_ports {la_out_p[11]}]
#set_property PACKAGE_PIN P20 [get_ports {la_out_p[12]}]
#set_property PACKAGE_PIN L17 [get_ports {la_out_p[13]}]
#set_property PACKAGE_PIN K19 [get_ports {la_out_p[14]}]
#set_property PACKAGE_PIN J16 [get_ports {la_out_p[15]}]
#set_property PACKAGE_PIN J20 [get_ports {la_out_p[16]}]

## FMC la	[17~33]
#set_property PACKAGE_PIN B19 [get_ports {la_in_p[0]}]
#set_property PACKAGE_PIN D20 [get_ports {la_in_p[1]}]
#set_property PACKAGE_PIN G15 [get_ports {la_in_p[2]}]
#set_property PACKAGE_PIN G20 [get_ports {la_in_p[3]}]
#set_property PACKAGE_PIN E19 [get_ports {la_in_p[4]}]
#set_property PACKAGE_PIN G19 [get_ports {la_in_p[5]}]
#set_property PACKAGE_PIN E15 [get_ports {la_in_p[6]}]
#set_property PACKAGE_PIN A18 [get_ports {la_in_p[7]}]
#set_property PACKAGE_PIN D22 [get_ports {la_in_p[8]}]
#set_property PACKAGE_PIN F18 [get_ports {la_in_p[9]}]
#set_property PACKAGE_PIN E21 [get_ports {la_in_p[10]}]
#set_property PACKAGE_PIN A16 [get_ports {la_in_p[11]}]
#set_property PACKAGE_PIN C17 [get_ports {la_in_p[12]}]
#set_property PACKAGE_PIN C15 [get_ports {la_in_p[13]}]
#set_property PACKAGE_PIN B16 [get_ports {la_in_p[15]}]
#set_property PACKAGE_PIN A21 [get_ports {la_in_p[14]}]
#set_property PACKAGE_PIN B21 [get_ports {la_in_p[16]}]

## JA2 Pi-CON
#set_property PACKAGE_PIN Y6   [get_ports {GPIO_4_GCLK}] 
#set_property PACKAGE_PIN AB10 [get_ports {GPIO_17}]  
#set_property PACKAGE_PIN AB9  [get_ports {GPIO_27}] 
#set_property PACKAGE_PIN AA6  [get_ports {GPIO_22}] 
#set_property PACKAGE_PIN Y10  [get_ports {GPIO_9}]  
#set_property PACKAGE_PIN Y11  [get_ports {GPIO_10}]
#set_property PACKAGE_PIN AB6  [get_ports {GPIO_11}] 
#set_property PACKAGE_PIN Y4   [get_ports {GPIO_5}] 
#set_property PACKAGE_PIN AA4  [get_ports {GPIO_6}] 
#set_property PACKAGE_PIN R6   [get_ports {GPIO_13}] 
#set_property PACKAGE_PIN T6   [get_ports {GPIO_19}]
#set_property PACKAGE_PIN U4   [get_ports {GPIO_26}]  

#set_property PACKAGE_PIN AA11 [get_ports {GPIO_14}]  
#set_property PACKAGE_PIN AB11 [get_ports {GPIO_15}]  
#set_property PACKAGE_PIN AA7  [get_ports {GPIO_18}] 
#set_property PACKAGE_PIN AB2  [get_ports {GPIO_23}] 
#set_property PACKAGE_PIN AB1  [get_ports {GPIO_24}] 
#set_property PACKAGE_PIN AB5  [get_ports {GPIO_25}] 
#set_property PACKAGE_PIN AB4  [get_ports {GPIO_8}] 
#set_property PACKAGE_PIN AB7  [get_ports {GPIO_7}]  
#set_property PACKAGE_PIN T4   [get_ports {GPIO_12}]  
#set_property PACKAGE_PIN V5   [get_ports {GPIO_16}]
#set_property PACKAGE_PIN V4   [get_ports {GPIO_20}] 
#set_property PACKAGE_PIN U6   [get_ports {GPIO_21}]

## DS1
#set_property PACKAGE_PIN U10  [get_ports {DSI_CLK_N}]  
#set_property PACKAGE_PIN U9   [get_ports {DSI_CLK_P}]  
#set_property PACKAGE_PIN V12  [get_ports {DSI_D0_N}]  
#set_property PACKAGE_PIN W12  [get_ports {DSI_D0_P}] 
#set_property PACKAGE_PIN U12  [get_ports {DSI_D1_N}]  
#set_property PACKAGE_PIN U11  [get_ports {DSI_D1_P}]  

#set_property PACKAGE_PIN W10  [get_ports {CAM_GPIO}}]
#set_property PACKAGE_PIN W11  [get_ports {CAM_CLK}]
#set_property PACKAGE_PIN AA8  [get_ports {CAM_CLK_N}]  
#set_property PACKAGE_PIN AA9  [get_ports {CAM_CLK_P}]  
#set_property PACKAGE_PIN V8   [get_ports {CAM_D1_P}]  
#set_property PACKAGE_PIN W8   [get_ports {CAM_D1_N}]
#set_property PACKAGE_PIN V10  [get_ports {CAM_D0_P}]  
#set_property PACKAGE_PIN V9   [get_ports {CAM_D0_N}}]

## XADC
#set_property PACKAGE_PIN H15 [get_ports {XADC_GIO0}]
#set_property PACKAGE_PIN R15 [get_ports {XADC_GIO1}]
#set_property PACKAGE_PIN K15 [get_ports {XADC_GIO2}]
#set_property PACKAGE_PIN J15 [get_ports {XADC_GIO3}]
