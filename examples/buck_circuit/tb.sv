// Steven Herbst
// sherbst@stanford.edu

`timescale 1ns/1ps

`include "svreal.sv"
`include "msdsl.sv"

`default_nettype none

module tb;
    // I/O definition
    `MAKE_CONST_REAL(5.0, v_in);
    `MAKE_REAL(v_out, 10.0);
    `MAKE_REAL(i_ind, 20.0);

    // Diode emulation comparison
    `MAKE_CONST_REAL(10e-3, ls_thresh);
    `GT_REAL(i_ind, ls_thresh, ls_en);

    // High-side signal
    `PWM(0.50, 500e3, hs);

    // Low-side signal
    logic ls;
    assign ls = (~hs) & ls_en;

    // buck instantiation
    buck #(
        `PASS_REAL(v_in, v_in),
        `PASS_REAL(v_out, v_out),
        `PASS_REAL(i_ind, i_ind)
    ) buck_i (
        .v_in(v_in),
        .v_out(v_out),
        .i_ind(i_ind),
        .hs(hs),
        .ls(ls)
    );

endmodule

`default_nettype wire