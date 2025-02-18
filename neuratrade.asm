; NeuraTrade AI trading strategy in Assembly x86
section .data
    ; Define constants
    buy_threshold equ 0.05
    sell_threshold equ 0.10

section .bss
    ; Reserve space for variables
    current_price resd 1
    previous_price resd 1

section .text
global _start

_start:
    ; Initialize variables
    mov dword [current_price], 0
    mov dword [previous_price], 0

loop_start:
    ; Get current price
    mov eax, 4        ; sys_read
    mov ebx, 0        ; file descriptor (stdin)
    mov ecx, current_price ; address of current_price
    mov edx, 4        ; length of current_price
    int 0x80

    ; Check if price has changed
    cmp dword [current_price], dword [previous_price]
    je loop_start     ; if not, loop back

    ; Update previous price
    mov eax, dword [current_price]
    mov dword [previous_price], eax

    ; Check if price has increased
    cmp dword [current_price], dword [previous_price]
    jle check_decrease ; if not, check if price has decreased

    ; Check if price increase is above buy threshold
    mov eax, dword [current_price]
    sub eax, dword [previous_price]
    cvtsi2sd xmm0, eax
    divsd xmm0, xmm1 ; xmm1 = previous_price
    comisd xmm0, [buy_threshold]
    jbe loop_start     ; if not, loop back

    ; Buy signal
    mov eax, 4        ; sys_write
    mov ebx, 1        ; file descriptor (stdout)
    mov ecx, buy_message ; address of buy message
    mov edx, 10       ; length of buy message
    int 0x80

    jmp loop_start

check_decrease:
    ; Check if price decrease is above sell threshold
    mov eax, dword [previous_price]
    sub eax, dword [current_price]
    cvtsi2sd xmm0, eax
    divsd xmm0, xmm1 ; xmm1 = previous_price
    comisd xmm0, [sell_threshold]
    jbe loop_start     ; if not, loop back

    ; Sell signal
    mov eax, 4        ; sys_write
    mov ebx, 1        ; file descriptor (stdout)
    mov ecx, sell_message ; address of sell message
    mov edx, 11       ; length of sell message
    int 0x80

    jmp loop_start

section .data
    buy_message db 'Buy signal', 0xa
    sell_message db 'Sell signal', 0xa
