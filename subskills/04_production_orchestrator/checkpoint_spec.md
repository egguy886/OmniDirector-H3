# Production Orchestrator Specification & State Schema

## 1. batch_progress.json Schema

```json
{
  "project": "Crossing_the_Line",
  "season": "S01",
  "episodes": {
    "E01": {
      "H3-01": {
        "status": "COMPLETED",
        "task_id": "comfy_task_98234710",
        "submitted_at": "2026-09-14T00:01:15+08:00",
        "completed_at": "2026-09-14T00:06:22+08:00",
        "video_path": "outputs/E01/E01_H3-01.mp4",
        "tail_frame_approved": true
      },
      "H3-02": {
        "status": "RUNNING",
        "task_id": "comfy_task_98234789",
        "submitted_at": "2026-09-14T00:06:25+08:00",
        "retry_count": 0
      }
    }
  }
}
```

## 2. CLI Execution Examples

### Unattended Overnight Run (Waiting for 00:01)
```bash
# Set your API key in environment
export MINIMAX_API_KEY="your_api_key_here"

# Run with macOS anti-sleep lock:
caffeinate -d -i -m -u python3 tools/run_overnight_batch.py
```

### Immediate Single-Episode Test
```bash
python3 tools/run_overnight_batch.py --immediate --episodes E01
```

### Dry-Run Verification (No API Spend)
```bash
python3 tools/run_overnight_batch.py --dry-run
```
