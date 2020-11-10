## Clock Source
set_property PACKAGE_PIN Y9 [get_ports {clk_ori}];  # "GCLK"
set_property IOSTANDARD LVCMOS25 [get_ports {clk_ori}]

set_property PACKAGE_PIN P16 [get_ports {reset}]
set_property IOSTANDARD LVCMOS25 [get_ports {reset}]

set_property PACKAGE_PIN Y5 [get_ports {hsync}]  
set_property IOSTANDARD LVCMOS25 [get_ports {hsync}]
set_property PACKAGE_PIN W5  [get_ports {vsync}] 
set_property IOSTANDARD LVCMOS25 [get_ports {vsync}]

set_property PACKAGE_PIN AA6  [get_ports {Bout}] 
set_property IOSTANDARD LVCMOS25 [get_ports {Bout}]
set_property PACKAGE_PIN AB9  [get_ports {Gout}] 
set_property IOSTANDARD LVCMOS25 [get_ports {Gout}]
set_property PACKAGE_PIN AB10  [get_ports {Rout}] 
set_property IOSTANDARD LVCMOS25 [get_ports {Rout}]



## JA2 Pi-CON
#set_property PACKAGE_PIN Y6   [get_ports {GPIO_4_GCLK}] 
#set_property PACKAGE_PIN AB10 [get_ports {Rout}]  
#set_property IOSTANDARD LVCMOS33 [get_ports {Rout}]
#set_property PACKAGE_PIN AB9  [get_ports {Gout}]
#set_property IOSTANDARD LVCMOS33 [get_ports {Gout}] 

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
#set_property PACKAGE_PIN AB2  [get_ports {Bout}] 
#set_property IOSTANDARD LVCMOS33 [get_ports {Bout}]
#set_property PACKAGE_PIN AB1  [get_ports {GPIO_24}] 
#set_property PACKAGE_PIN AB5  [get_ports {GPIO_25}] 
#set_property PACKAGE_PIN AB4  [get_ports {GPIO_8}] 
#set_property PACKAGE_PIN AB7  [get_ports {GPIO_7}]  
#set_property PACKAGE_PIN T4   [get_ports {GPIO_12}]  
#set_property PACKAGE_PIN V5   [get_ports {GPIO_16}]
#set_property PACKAGE_PIN V4   [get_ports {GPIO_20}] 
#set_property PACKAGE_PIN U6   [get_ports {GPIO_21}]
