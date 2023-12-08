#include <stdio.h>
#include "pico/stdlib.h"

int main() {

    const uint led_pin = 6; //4;//25

    gpio_init(led_pin);
    gpio_set_dir(led_pin, GPIO_OUT);


    setup_default_uart();
    printf("Hello, world!\n");
    
    while(1){
        gpio_put(led_pin,true);
        sleep_ms(1000);

        gpio_put(led_pin,false);
        sleep_ms(1000);
    }

    return 0;
}