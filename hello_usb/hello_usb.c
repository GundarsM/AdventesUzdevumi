/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    const uint led_pin = 6;//25

    gpio_init(led_pin);
    gpio_set_dir(led_pin, GPIO_OUT);


    stdio_init_all();
    while (true) {

        gpio_put(led_pin,true);
        printf("Hello, world!\n");
        sleep_ms(1000);

        gpio_put(led_pin,false);
        sleep_ms(1000);
    }
}