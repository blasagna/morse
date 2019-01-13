package main

import (
	"flag"
	"fmt"
	"strings"
	"time"

	"github.com/blasagna/morse"
	termbox "github.com/nsf/termbox-go"
)

var dotFlag string
var dashFlag string
var quitFlag string
var timeoutFlag time.Duration

func init() {
	flag.StringVar(&dotFlag, "dot", "j", "Dot input. Valid options are single character inputs.")
	flag.StringVar(&dashFlag, "dash", "k", "Dash input. Valid options are single character inputs.")
	flag.StringVar(&quitFlag, "quit", "q", "Quit input. Valid options are single character inputs.")
	flag.DurationVar(&timeoutFlag, "timeout", time.Duration(300)*time.Millisecond, "Input timeout duration")
}

func main() {
	flag.Parse()
	timeoutInput := timeoutFlag
	quitInput := []rune(quitFlag)[0]
	dotInput := []rune(dotFlag)[0]
	dashInput := []rune(dashFlag)[0]

	err := termbox.Init()
	if err != nil {
		panic(err)
	}
	defer termbox.Close()

	eventQueue := make(chan termbox.Event)
	go func() {
		for {
			eventQueue <- termbox.PollEvent()
		}
	}()

	termbox.SetInputMode(termbox.InputMouse)
	termbox.Clear(termbox.ColorDefault, termbox.ColorDefault)

	seqInput := []morse.InputEvent{}
	lastInputTime := time.Now()

	fmt.Println("We \u2661  Morse code!")
	fmt.Println("Current config:")
	fmt.Println("Dot:", string(dotInput))
	fmt.Println("Dash:", string(dashInput))
	fmt.Println("Input timeout:", timeoutInput)
	fmt.Println("Quit:", string(quitInput))
	fmt.Println()

	outputBuilder := strings.Builder{}
inputloop:
	for {
		select {
		case ev := <-eventQueue:
			if ev.Type == termbox.EventKey {
				if ev.Ch < 128 {
					switch ev.Ch {
					case dotInput:
						seqInput = append(seqInput, morse.Dot)
					case dashInput:
						seqInput = append(seqInput, morse.Dash)
					case quitInput:
						break inputloop
					}
					lastInputTime = time.Now()
				}
			}
			if ev.Type == termbox.EventError {
				panic(ev.Err)
			}
		default:
			if len(seqInput) > 0 && time.Since(lastInputTime) > timeoutInput {
				output := morse.Decode(seqInput)
				outputBuilder.WriteString(output)
				fmt.Println(seqInput, output)
				fmt.Println(outputBuilder.String())
				lastInputTime = time.Now()
				seqInput = nil
			}
		}
		termbox.Flush()
	}
} // main
