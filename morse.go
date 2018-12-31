package morse

// todo next: build library to process sequences of inputs

import (
	"reflect"
)

type MorseEvent int

const (
	Dot     MorseEvent = 0
	Dash    MorseEvent = 1
	Invalid MorseEvent = 2
)

type MorseSequence struct {
	Output string
	Seq    []MorseEvent
}

var E = MorseSequence{"e", []MorseEvent{Dot}}
var T = MorseSequence{"t", []MorseEvent{Dash}}
var SeqLen1 = []MorseSequence{E, T}
var I = MorseSequence{"i", []MorseEvent{Dot, Dot}}
var A = MorseSequence{"a", []MorseEvent{Dot, Dash}}
var N = MorseSequence{"n", []MorseEvent{Dash, Dot}}
var M = MorseSequence{"m", []MorseEvent{Dash, Dash}}
var SeqLen2 = []MorseSequence{I, A, N, M}
var S = MorseSequence{"s", []MorseEvent{Dot, Dot, Dot}}
var U = MorseSequence{"u", []MorseEvent{Dot, Dot, Dash}}
var R = MorseSequence{"r", []MorseEvent{Dot, Dash, Dot}}
var W = MorseSequence{"w", []MorseEvent{Dot, Dash, Dash}}
var D = MorseSequence{"d", []MorseEvent{Dash, Dot, Dot}}
var K = MorseSequence{"k", []MorseEvent{Dash, Dot, Dash}}
var G = MorseSequence{"g", []MorseEvent{Dash, Dash, Dot}}
var O = MorseSequence{"o", []MorseEvent{Dash, Dash, Dash}}
var SeqLen3 = []MorseSequence{S, U, R, W, D, K, G, O}
var H = MorseSequence{"h", []MorseEvent{Dot, Dot, Dot, Dot}}
var V = MorseSequence{"v", []MorseEvent{Dot, Dot, Dot, Dash}}
var F = MorseSequence{"f", []MorseEvent{Dot, Dot, Dash, Dot}}
var Space = MorseSequence{" ", []MorseEvent{Dot, Dot, Dash, Dash}}
var L = MorseSequence{"l", []MorseEvent{Dot, Dash, Dot, Dot}}

// unused MorseSequence{"", []MorseEvent{Dot, Dash, Dot, Dash}}
var P = MorseSequence{"p", []MorseEvent{Dot, Dash, Dash, Dot}}
var J = MorseSequence{"j", []MorseEvent{Dot, Dash, Dash, Dash}}
var B = MorseSequence{"b", []MorseEvent{Dash, Dot, Dot, Dot}}
var X = MorseSequence{"x", []MorseEvent{Dash, Dot, Dot, Dash}}
var C = MorseSequence{"c", []MorseEvent{Dash, Dot, Dash, Dot}}
var Y = MorseSequence{"y", []MorseEvent{Dash, Dot, Dash, Dash}}
var Z = MorseSequence{"z", []MorseEvent{Dash, Dash, Dot, Dot}}
var Q = MorseSequence{"q", []MorseEvent{Dash, Dash, Dot, Dash}}

// unused MorseSequence{"", []MorseEvent{Dash, Dash, Dash, Dot}}
var Back = MorseSequence{"\b", []MorseEvent{Dash, Dash, Dash, Dash}}
var SeqLen4 = []MorseSequence{H, V, F, Space, L, P, J, B, X, C, Y, Z, Q, Back}

var Zero = MorseSequence{"0", []MorseEvent{Dash, Dash, Dash, Dash, Dash}}
var One = MorseSequence{"1", []MorseEvent{Dot, Dash, Dash, Dash, Dash}}
var Two = MorseSequence{"2", []MorseEvent{Dot, Dot, Dash, Dash, Dash}}
var Three = MorseSequence{"3", []MorseEvent{Dot, Dot, Dot, Dash, Dash}}
var Four = MorseSequence{"4", []MorseEvent{Dot, Dot, Dot, Dot, Dash}}
var Five = MorseSequence{"5", []MorseEvent{Dot, Dot, Dot, Dot, Dot}}
var Six = MorseSequence{"6", []MorseEvent{Dash, Dot, Dot, Dot, Dot}}
var Seven = MorseSequence{"7", []MorseEvent{Dash, Dash, Dot, Dot, Dot}}
var Eight = MorseSequence{"8", []MorseEvent{Dash, Dash, Dash, Dot, Dot}}
var Nine = MorseSequence{"9", []MorseEvent{Dash, Dash, Dash, Dash, Dot}}
var SeqLen5 = []MorseSequence{Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine}

var SeqAll = [][]MorseSequence{SeqLen1, SeqLen2, SeqLen3, SeqLen4, SeqLen5}

const SeqLenMax = 5
const OutputInvalid = ""

func Decode(s []MorseEvent) string {
	out := OutputInvalid

	// truncate input to max length
	s = s[:SeqLenMax]

	for _, candidate := range SeqAll[len(s)-1] {
		if reflect.DeepEqual(candidate.Seq, s) {
			out = candidate.Output
			break
		}
	}
	return out
}

// func main() {
// 	for _, list := range(SeqAll) {
// 		for _, v := range(list) {
// 			fmt.Println(v.Output, v.Seq)
// 		}
// 	}
// }
