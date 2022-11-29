### arch/arm/boot/dts/am335x-bone-common-univ.dtsi

```
		/* P9_30 (ZCZ ball D12) gpio3_16 */
	P9_30_default_pin: pinmux_P9_30_default_pin { pinctrl-single,pins = <
		P9_30( PIN_OUTPUT_PULLDOWN | INPUT_EN | MUX_MODE7) >; };	/* mcasp0_axr0.gpio3_16 */
	P9_30_gpio_pin: pinmux_P9_30_gpio_pin { pinctrl-single,pins = <
		P9_30( PIN_OUTPUT | INPUT_EN | MUX_MODE7) >; };		/* mcasp0_axr0.gpio3_16 */
	P9_30_gpio_pu_pin: pinmux_P9_30_gpio_pu_pin { pinctrl-single,pins = <
		P9_30( PIN_OUTPUT_PULLUP | INPUT_EN | MUX_MODE7) >; };	/* mcasp0_axr0.gpio3_16 */
	P9_30_gpio_pd_pin: pinmux_P9_30_gpio_pd_pin { pinctrl-single,pins = <
		P9_30( PIN_OUTPUT_PULLDOWN | INPUT_EN | MUX_MODE7) >; };	/* mcasp0_axr0.gpio3_16 */
	P9_30_pwm_pin: pinmux_P9_30_pwm_pin { pinctrl-single,pins = <
		P9_30( PIN_OUTPUT_PULLDOWN | INPUT_EN | MUX_MODE1) >; };	/* mcasp0_axr0.ehrpwm0_tripzone_input */
	P9_30_spi_pin: pinmux_P9_30_spi_pin { pinctrl-single,pins = <
		P9_30( PIN_OUTPUT_PULLUP | INPUT_EN | MUX_MODE3) >; };	/* mcasp0_axr0.spi1_d1 */
	P9_30_pruout_pin: pinmux_P9_30_pruout_pin { pinctrl-single,pins = <
		P9_30( PIN_OUTPUT_PULLDOWN | INPUT_EN | MUX_MODE5) >; };	/* mcasp0_axr0.pru0_out2 */
	P9_30_pruin_pin: pinmux_P9_30_pruin_pin { pinctrl-single,pins = <
		P9_30( PIN_INPUT | MUX_MODE6) >; };			/* mcasp0_axr0.pru0_in2 */
	P9_30_mcasp_pin: pinmux_P9_30_mcasp_pin { pinctrl-single,pins = <
		P9_30( PIN_INPUT_PULLDOWN | MUX_MODE0) >; };			/* mcasp0_axr0.mcasp0_axr0 */
```

```
	/* P9_30 (ZCZ ball D12) */
	P9_30_pinmux {
		compatible = "bone-pinmux-helper";
		status = "okay";
		pinctrl-names = "default", "gpio", "gpio_pu", "gpio_pd", "spi", "pwm", "pruout", "pruin";
		pinctrl-0 = <&P9_30_default_pin>;
		pinctrl-1 = <&P9_30_gpio_pin>;
		pinctrl-2 = <&P9_30_gpio_pu_pin>;
		pinctrl-3 = <&P9_30_gpio_pd_pin>;
		pinctrl-4 = <&P9_30_spi_pin>;
		pinctrl-5 = <&P9_30_pwm_pin>;
		pinctrl-6 = <&P9_30_pruout_pin>;
		pinctrl-7 = <&P9_30_pruin_pin>;
		pinctrl-8 = <&P9_30_mcasp_pin>;
	};
```





#### BB-RAYSTAR-TOUCHPAD-00A0.dts

```
fragment@0 {
		target = <&ocp>;
		__overlay__ {
			P8_45_pinmux { status = "disabled"; };	/* lcd: lcd_data0 */
			P8_46_pinmux { status = "disabled"; };	/* lcd: lcd_data1 */
			P8_43_pinmux { status = "disabled"; };	/* lcd: lcd_data2 */
			P8_44_pinmux { status = "disabled"; };	/* lcd: lcd_data3 */
			P8_41_pinmux { status = "disabled"; };	/* lcd: lcd_data4 */
			P8_42_pinmux { status = "disabled"; };	/* lcd: lcd_data5 */
			P8_39_pinmux { status = "disabled"; };	/* lcd: lcd_data6 */
			P8_40_pinmux { status = "disabled"; };	/* lcd: lcd_data7 */
			P8_37_pinmux { status = "disabled"; };	/* lcd: lcd_data8 */
			P8_38_pinmux { status = "disabled"; };	/* lcd: lcd_data9 */
			P8_36_pinmux { status = "disabled"; };	/* lcd: lcd_data10 */
			P8_34_pinmux { status = "disabled"; };	/* lcd: lcd_data11 */
			P8_35_pinmux { status = "disabled"; };	/* lcd: lcd_data12 */
			P8_33_pinmux { status = "disabled"; };	/* lcd: lcd_data13 */
			P8_31_pinmux { status = "disabled"; };	/* lcd: lcd_data14 */
			P8_32_pinmux { status = "disabled"; };	/* lcd: lcd_data15 */
			P8_15_pinmux { status = "disabled"; };	/* lcd: lcd_data16 */
			P8_16_pinmux { status = "disabled"; };	/* lcd: lcd_data17 */
			P8_11_pinmux { status = "disabled"; };	/* lcd: lcd_data18 */
			P8_12_pinmux { status = "disabled"; };	/* lcd: lcd_data19 */
			P8_17_pinmux { status = "disabled"; };	/* lcd: lcd_data20 */
			P8_14_pinmux { status = "disabled"; };	/* lcd: lcd_data21 */
			P8_13_pinmux { status = "disabled"; };	/* lcd: lcd_data22 */
			P8_19_pinmux { status = "disabled"; };	/* lcd: lcd_data23 */
			P8_27_pinmux { status = "disabled"; };	/* lcd: lcd_vsync */
			P8_29_pinmux { status = "disabled"; };	/* lcd: lcd_hsync */
			P8_28_pinmux { status = "disabled"; };	/* lcd: lcd_pclk */
			P8_30_pinmux { status = "disabled"; };	/* lcd: lcd_ac_bias_en */

			P9_27_pinmux { status = "disabled"; };	/* lcd: lcd_disp */

			P9_42_pinmux { status = "disabled"; };	/* pwm: eCAP0_in_PWM2_out */
			P9_23_pinmux { status = "disabled"; };  /* lcd: lcd power switch */

			P9_15_pinmux { status = "disabled"; };	/* touch reset: gpio1_16 */
			P9_16_pinmux { status = "disabled"; };	/* touch interrupt: gpio1_19 */
			
			P9_30_pinmux { pinctrl-0 = <&P9_30_gpio_pd_pin>; } /* gpio output pull-down */
		};
	};
```

