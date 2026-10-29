
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


def main():
    reference_data = pd.DataFrame({
        "value": [10, 11, 12, 10, 11, 12, 10, 11, 12, 10]
    })

    current_data = pd.DataFrame({
        "value": [20, 21, 22, 20, 21, 22, 20, 21, 22, 20]
    })

    report = Report([
        DataDriftPreset()
    ])

    snapshot = report.run(
        reference_data=reference_data,
        current_data=current_data
    )

    snapshot.save_html("evidently_report.html")

    print("Evidently monitoring report generated.")
    print("Open evidently_report.html to inspect the report.")


if __name__ == "__main__":
    main()
