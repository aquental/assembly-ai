package main

import (
    "context"
    "fmt"
    "os"

    aai "github.com/AssemblyAI/assemblyai-go-sdk"
)

func main() {
    ctx := context.Background()

    audioURL := "https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3"

    client := aai.NewClient("YOUR_API_KEY")

    params := &aai.TranscriptOptionalParams{
        SpeakerLabels: aai.Bool(true),
    }

    transcript, err := client.Transcripts.TranscribeFromURL(ctx, audioURL, params)
    if err != nil {
        fmt.Println("Something bad happened:", err)
        os.Exit(1)
    }

    fmt.Println(*transcript.Text)

    for _, utterance := range transcript.Utterances {
        fmt.Printf("Speaker %v: %v\n", *utterance.Speaker, *utterance.Text)
    }
}
