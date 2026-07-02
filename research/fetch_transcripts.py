"""
fetch_transcripts.py
Automatically fetches YouTube video transcripts and saves each one as a
.md file, for the AI-powered SEO content production research project.

Usage:
1. pip install youtube-transcript-api
2. Fill in the VIDEOS dictionary below: "expert_name": ["video_id_1", "video_id_2", ...]
3. Run: python fetch_transcripts.py
"""

import os
from youtube_transcript_api import YouTubeTranscriptApi

VIDEOS = {
    "kevin-indig": [
        "jxXPpXL2pFg",
        "c-VtgjXWsK4",
    ],
    "lily-ray": [
        "c-VtgjXWsK4",
    ],
    "garrett-sussman": [
        "arAxL5MteVg",
    ],
    "britney-muller": [
        "l4fIHPtjIMY",
        "YZD2lmcbryo",
        "N2fb2b_hSOU",
    ],
    "aleyda-solis": [
        # Visit https://www.youtube.com/c/CrawlingMondaysbyAleyda
        # pick a recent video and add its Video ID here
    ],
}

OUTPUT_DIR = "research/youtube-transcripts"


def fetch_and_save(expert_name, video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = "\n".join([entry["text"] for entry in transcript])

        expert_dir = os.path.join(OUTPUT_DIR, expert_name)
        os.makedirs(expert_dir, exist_ok=True)

        output_path = os.path.join(expert_dir, f"{video_id}.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"# Transcript: {video_id}\n")
            f.write(f"**Expert:** {expert_name}\n")
            f.write(f"**Video URL:** https://youtube.com/watch?v={video_id}\n\n")
            f.write("---\n\n")
            f.write(full_text)

        print(f"✅ Saved: {output_path}")

    except Exception as e:
        print(f"❌ Failed for {video_id} ({expert_name}): {e}")


if __name__ == "__main__":
    for expert, video_ids in VIDEOS.items():
        for vid in video_ids:
            fetch_and_save(expert, vid)

    print("\nDone. Check the research/youtube-transcripts/ folder.")
