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

var chE = morseSequence{"e", []InputEvent{Dot}}
var chT = morseSequence{"t", []InputEvent{Dash}}
var seqLen1 = []morseSequence{chE, chT}
var chI = morseSequence{"i", []InputEvent{Dot, Dot}}
var chA = morseSequence{"a", []InputEvent{Dot, Dash}}
var chN = morseSequence{"n", []InputEvent{Dash, Dot}}
var chM = morseSequence{"m", []InputEvent{Dash, Dash}}
var seqLen2 = []morseSequence{chI, chA, chN, chM}
var chS = morseSequence{"s", []InputEvent{Dot, Dot, Dot}}
var chU = morseSequence{"u", []InputEvent{Dot, Dot, Dash}}
var chR = morseSequence{"r", []InputEvent{Dot, Dash, Dot}}
var chW = morseSequence{"w", []InputEvent{Dot, Dash, Dash}}
var chD = morseSequence{"d", []InputEvent{Dash, Dot, Dot}}
var chK = morseSequence{"k", []InputEvent{Dash, Dot, Dash}}
var chG = morseSequence{"g", []InputEvent{Dash, Dash, Dot}}
var chO = morseSequence{"o", []InputEvent{Dash, Dash, Dash}}
var seqLen3 = []morseSequence{chS, chU, chR, chW, chD, chK, chG, chO}
var chH = morseSequence{"h", []InputEvent{Dot, Dot, Dot, Dot}}
var chV = morseSequence{"v", []InputEvent{Dot, Dot, Dot, Dash}}
var chF = morseSequence{"f", []InputEvent{Dot, Dot, Dash, Dot}}
var chSpace = morseSequence{" ", []InputEvent{Dot, Dot, Dash, Dash}}
var chL = morseSequence{"l", []InputEvent{Dot, Dash, Dot, Dot}}

// unused morseSequence{"", []InputEvent{Dot, Dash, Dot, Dash}}
var chP = morseSequence{"p", []InputEvent{Dot, Dash, Dash, Dot}}
var chJ = morseSequence{"j", []InputEvent{Dot, Dash, Dash, Dash}}
var chB = morseSequence{"b", []InputEvent{Dash, Dot, Dot, Dot}}
var chX = morseSequence{"x", []InputEvent{Dash, Dot, Dot, Dash}}
var chC = morseSequence{"c", []InputEvent{Dash, Dot, Dash, Dot}}
var chY = morseSequence{"y", []InputEvent{Dash, Dot, Dash, Dash}}
var chZ = morseSequence{"z", []InputEvent{Dash, Dash, Dot, Dot}}
var chQ = morseSequence{"q", []InputEvent{Dash, Dash, Dot, Dash}}

// unused morseSequence{"", []InputEvent{Dash, Dash, Dash, Dot}}
var chBack = morseSequence{"\b", []InputEvent{Dash, Dash, Dash, Dash}}
var seqLen4 = []morseSequence{chH, chV, chF, chSpace, chL, chP, chJ, chB, chX, chC, chY, chZ, chQ, chBack}

var digit0 = morseSequence{"0", []InputEvent{Dash, Dash, Dash, Dash, Dash}}
var digit1 = morseSequence{"1", []InputEvent{Dot, Dash, Dash, Dash, Dash}}
var digit2 = morseSequence{"2", []InputEvent{Dot, Dot, Dash, Dash, Dash}}
var digit3 = morseSequence{"3", []InputEvent{Dot, Dot, Dot, Dash, Dash}}
var digit4 = morseSequence{"4", []InputEvent{Dot, Dot, Dot, Dot, Dash}}
var digit5 = morseSequence{"5", []InputEvent{Dot, Dot, Dot, Dot, Dot}}
var digit6 = morseSequence{"6", []InputEvent{Dash, Dot, Dot, Dot, Dot}}
var digit7 = morseSequence{"7", []InputEvent{Dash, Dash, Dot, Dot, Dot}}
var digit8 = morseSequence{"8", []InputEvent{Dash, Dash, Dash, Dot, Dot}}
var digit9 = morseSequence{"9", []InputEvent{Dash, Dash, Dash, Dash, Dot}}
var seqLen5 = []morseSequence{digit0, digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9}

var seqAll = [][]morseSequence{seqLen1, seqLen2, seqLen3, seqLen4, seqLen5}

const seqLenMax = 5
const outputInvalid = ""

// Decode converts valid Morse code input into an output character.
// If the sequence is not valid an empty string is returned.
func Decode(s []InputEvent) string {
	out := outputInvalid

	// truncate input to max length
	if len(s) > seqLenMax {
		s = s[:seqLenMax]
	}

	if len(s) > 0 {
		for _, candidate := range seqAll[len(s)-1] {
			if reflect.DeepEqual(candidate.Seq, s) {
				out = candidate.Output
				break
			}
		}
	}
	return out
}
