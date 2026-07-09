package morse

import (
	"testing"
)

func TestDecodeValid(t *testing.T) {
	for _, list := range seqAll {
		for _, v := range list {
			if Decode(v.Seq) != v.Output {
				t.Error("Decode vaild input failed")
			}
		}
	}
}

func TestDecodeInvalid(t *testing.T) {
	inputInvalid := []InputEvent{Dot, Dash, 12, 'c', Invalid}
	if Decode(inputInvalid) != "" {
		t.Error("Decode invalid input failed")
	}
}

func TestDecodeLong(t *testing.T) {
	inputLong := []InputEvent{Dot, Dot, Dot, Dot, Dot, Invalid}
	if Decode(inputLong) != "5" {
		t.Error("Decode long input failed")
	}
}

func TestDecodeEmpty(t *testing.T) {
	inputEmpty := []InputEvent{}
	if Decode(inputEmpty) != "" {
		t.Error("Decode empty input failed")
	}

}
