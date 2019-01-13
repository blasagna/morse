package main

import (
	"fmt"
	"time"

	"github.com/blasagna/morse"
	termbox "github.com/nsf/termbox-go"
)

func main() {

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
	timeoutInput := 0.3
	quitInput := 'q'
	dotInput := 'j'
	dashInput := 'k'

	fmt.Println("We \u2661  Morse code!")
	fmt.Println("Current config:")
	fmt.Println("Dot:", string(dotInput))
	fmt.Println("Dash:", string(dashInput))
	fmt.Println("Quit:", string(quitInput))
	fmt.Println()
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
						fmt.Println("quitting...")
						break inputloop
					}
					lastInputTime = time.Now()
				}
			}
			// TODO: configure to use mouse buttons as input
			if ev.Type == termbox.EventMouse {
				switch ev.Key {
				case termbox.MouseLeft:
					fmt.Println("mouse left")
					termbox.Flush()
				case termbox.MouseRight:
					fmt.Println("mouse right")
					termbox.Flush()
				}
			}
			if ev.Type == termbox.EventError {
				panic(ev.Err)
			}
		default:
			if len(seqInput) > 0 && time.Since(lastInputTime).Seconds() > timeoutInput {
				fmt.Print(morse.Decode(seqInput))
				lastInputTime = time.Now()
				seqInput = nil
			}
		}
		termbox.Flush()
	}
} // main
