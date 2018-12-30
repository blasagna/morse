package main

// todo next: build library to process sequences of inputs

import (
	"fmt"

	"github.com/nsf/termbox-go"
)

func main() {
	fmt.Println("hello!")

	err := termbox.Init()
	if err != nil {
		panic(err)
	}
	defer termbox.Close()

	termbox.SetInputMode(termbox.InputMouse)
	termbox.Clear(termbox.ColorDefault, termbox.ColorDefault)
inputloop:
	for {
		switch ev := termbox.PollEvent(); ev.Type {
		case termbox.EventKey:
			if ev.Ch < 128 {
				switch ev.Ch {
				case 'j':
					fmt.Println("pressed j")
					termbox.Flush()
				case 'k':
					fmt.Println("pressed k")
					termbox.Flush()
				case 'q':
					fmt.Println("quitting...")
					termbox.Flush()
					break inputloop
				}
			}
		case termbox.EventMouse:
			switch ev.Key {
			case termbox.MouseLeft:
				fmt.Println("mouse left")
				termbox.Flush()
			case termbox.MouseRight:
				fmt.Println("mouse right")
				termbox.Flush()
			}
		case termbox.EventError:
			panic(ev.Err)
		}
	}

	fmt.Println("done.")
}
