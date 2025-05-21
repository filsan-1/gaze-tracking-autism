def log_fixation_data(ts, target, pt):
    with open("gaze_fixations.csv", 'a', newline='') as f:
        import csv
        csv.writer(f).writerow([ts, target, int(pt[0]), int(pt[1])])

def get_fixation_stats(counter, duration_sec):
    # Normalize fixation counts to % time
    total = sum(counter.values()) or 1
    perc = {k: round(v / total * 100, 2) for k, v in counter.items()}

    # Risk score logic
    score = 0
    if perc['eyes_left'] + perc['eyes_right'] < 30:
        score += 3  # low eye contact
    if perc['none'] > 40:
        score += 3  # unfocused or random gaze
    if perc['mouth'] < 10:
        score += 2  # low interest in social cues
    if duration_sec < 60:
        score += 2  # too short session

    # Determine risk level
    if score <= 3:
        level = "🟢 Low Risk"
    elif score <= 6:
        level = "🟡 Moderate Risk"
    else:
        level = "🔴 High Risk - Consider professional evaluation"

    report = f"""
    -------- Autism Gaze Screening Report --------
    Eyes Fixation: {perc['eyes_left'] + perc['eyes_right']}%
    Mouth Fixation: {perc['mouth']}%
    Nose Fixation: {perc['nose']}%
    Unfocused Gaze: {perc['none']}%
    Total Time: {round(duration_sec, 1)} sec

    📈 Autism Risk Score: {score}/10
    🧠 Risk Level: {level}
    ----------------------------------------------
    """

    return score, report

