## Clock Source
set_property PACKAGE_PIN Y9 [get_ports {clk}]
set_property IOSTANDARD LVCMOS33 [get_ports {clk}]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets reset_IBUF]

## reset btw
set_property -dict {PACKAGE_PIN P16 IOSTANDARD LVCMOS33} [get_ports {reset}]

## ledout
set_property -dict {PACKAGE_PIN T22 IOSTANDARD LVCMOS33} [get_ports {ledout[0]}]
set_property -dict {PACKAGE_PIN T21 IOSTANDARD LVCMOS33} [get_ports {ledout[1]}]
set_property -dict {PACKAGE_PIN U22 IOSTANDARD LVCMOS33} [get_ports {ledout[2]}]
set_property -dict {PACKAGE_PIN U21 IOSTANDARD LVCMOS33} [get_ports {ledout[3]}]
set_property -dict {PACKAGE_PIN V22 IOSTANDARD LVCMOS33} [get_ports {ledout[4]}]
set_property -dict {PACKAGE_PIN W22 IOSTANDARD LVCMOS33} [get_ports {ledout[5]}]
set_property -dict {PACKAGE_PIN U19 IOSTANDARD LVCMOS33} [get_ports {ledout[6]}]
set_property -dict {PACKAGE_PIN U14 IOSTANDARD LVCMOS33} [get_ports {ledout[7]}]

## seven-segment display
set_property -dict {PACKAGE_PIN U10 IOSTANDARD LVCMOS33} [get_ports {sevenout[0]}]
set_property -dict {PACKAGE_PIN U9 IOSTANDARD LVCMOS33} [get_ports {sevenout[1]}]
set_property -dict {PACKAGE_PIN AA12 IOSTANDARD LVCMOS33} [get_ports {sevenout[2]}]
set_property -dict {PACKAGE_PIN W12 IOSTANDARD LVCMOS33} [get_ports {sevenout[3]}]
set_property -dict {PACKAGE_PIN V12 IOSTANDARD LVCMOS33} [get_ports {sevenout[4]}]
set_property -dict {PACKAGE_PIN U11 IOSTANDARD LVCMOS33} [get_ports {sevenout[5]}]
set_property -dict {PACKAGE_PIN U12 IOSTANDARD LVCMOS33} [get_ports {sevenout[6]}]
