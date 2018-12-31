// Package morse decodes Morse code
package morse

import (
	"reflect"
)

// InputEvent is an input event
type InputEvent int

const (
	// Dot input event
	Dot InputEvent = 0
	// Dash input event
	Dash InputEvent = 1
	// Invalid (not dot/dash) input event
	Invalid InputEvent = 2
)

type morseSequence struct {
	Output string
	Seq    []InputEvent
}

var e = morseSequence{"e", []InputEvent{Dot}}
var t = morseSequence{"t", []InputEvent{Dash}}
var seqLen1 = []morseSequence{e, t}
var i = morseSequence{"i", []InputEvent{Dot, Dot}}
var a = morseSequence{"a", []InputEvent{Dot, Dash}}
var n = morseSequence{"n", []InputEvent{Dash, Dot}}
var m = morseSequence{"m", []InputEvent{Dash, Dash}}
var seqLen2 = []morseSequence{i, a, n, m}
var s = morseSequence{"s", []InputEvent{Dot, Dot, Dot}}
var u = morseSequence{"u", []InputEvent{Dot, Dot, Dash}}
var r = morseSequence{"r", []InputEvent{Dot, Dash, Dot}}
var w = morseSequence{"w", []InputEvent{Dot, Dash, Dash}}
var d = morseSequence{"d", []InputEvent{Dash, Dot, Dot}}
var k = morseSequence{"k", []InputEvent{Dash, Dot, Dash}}
var g = morseSequence{"g", []InputEvent{Dash, Dash, Dot}}
var o = morseSequence{"o", []InputEvent{Dash, Dash, Dash}}
var seqLen3 = []morseSequence{s, u, r, w, d, k, g, o}
var h = morseSequence{"h", []InputEvent{Dot, Dot, Dot, Dot}}
var v = morseSequence{"v", []InputEvent{Dot, Dot, Dot, Dash}}
var f = morseSequence{"f", []InputEvent{Dot, Dot, Dash, Dot}}
var space = morseSequence{" ", []InputEvent{Dot, Dot, Dash, Dash}}
var l = morseSequence{"l", []InputEvent{Dot, Dash, Dot, Dot}}

// unused morseSequence{"", []InputEvent{Dot, Dash, Dot, Dash}}
var p = morseSequence{"p", []InputEvent{Dot, Dash, Dash, Dot}}
var j = morseSequence{"j", []InputEvent{Dot, Dash, Dash, Dash}}
var b = morseSequence{"b", []InputEvent{Dash, Dot, Dot, Dot}}
var x = morseSequence{"x", []InputEvent{Dash, Dot, Dot, Dash}}
var c = morseSequence{"c", []InputEvent{Dash, Dot, Dash, Dot}}
var y = morseSequence{"y", []InputEvent{Dash, Dot, Dash, Dash}}
var z = morseSequence{"z", []InputEvent{Dash, Dash, Dot, Dot}}
var q = morseSequence{"q", []InputEvent{Dash, Dash, Dot, Dash}}

// unused morseSequence{"", []InputEvent{Dash, Dash, Dash, Dot}}
var back = morseSequence{"\b", []InputEvent{Dash, Dash, Dash, Dash}}
var seqLen4 = []morseSequence{h, v, f, space, l, p, j, b, x, c, y, z, q, back}

var zero = morseSequence{"0", []InputEvent{Dash, Dash, Dash, Dash, Dash}}
var one = morseSequence{"1", []InputEvent{Dot, Dash, Dash, Dash, Dash}}
var two = morseSequence{"2", []InputEvent{Dot, Dot, Dash, Dash, Dash}}
var three = morseSequence{"3", []InputEvent{Dot, Dot, Dot, Dash, Dash}}
var four = morseSequence{"4", []InputEvent{Dot, Dot, Dot, Dot, Dash}}
var five = morseSequence{"5", []InputEvent{Dot, Dot, Dot, Dot, Dot}}
var six = morseSequence{"6", []InputEvent{Dash, Dot, Dot, Dot, Dot}}
var seven = morseSequence{"7", []InputEvent{Dash, Dash, Dot, Dot, Dot}}
var eight = morseSequence{"8", []InputEvent{Dash, Dash, Dash, Dot, Dot}}
var nine = morseSequence{"9", []InputEvent{Dash, Dash, Dash, Dash, Dot}}
var seqLen5 = []morseSequence{zero, one, two, three, four, five, six, seven, eight, nine}

var seqAll = [][]morseSequence{seqLen1, seqLen2, seqLen3, seqLen4, seqLen5}

const seqLenMax = 5
const outputInvalid = ""

// Decode converts valid Morse code input into an output character.
// If the sequence is not valid an empty string is returned.
func Decode(s []InputEvent) string {
	out := outputInvalid

	// truncate input to max length
	s = s[:seqLenMax]

	for _, candidate := range seqAll[len(s)-1] {
		if reflect.DeepEqual(candidate.Seq, s) {
			out = candidate.Output
			break
		}
	}
	return out
}
