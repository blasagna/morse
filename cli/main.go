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
	fmt.Println("hello!")

	seqInput := []morse.InputEvent{}
	lastInputTime := time.Now()
	timeoutInput := 0.5
inputloop:
	for {
		select {
		case ev := <-eventQueue:
			if ev.Type == termbox.EventKey {
				if ev.Ch < 128 {
					switch ev.Ch {
					case 'j':
						fmt.Println("pressed j")
						seqInput = append(seqInput, morse.Dot)
					case 'k':
						fmt.Println("pressed k")
						seqInput = append(seqInput, morse.Dash)
					case 'q':
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
			if time.Since(lastInputTime).Seconds() > timeoutInput {
				// TODO: decode input sequence
				fmt.Println(seqInput, time.Since(lastInputTime))
				lastInputTime = time.Now()
				seqInput = nil
			}
		}
		termbox.Flush()
	}
} // main
