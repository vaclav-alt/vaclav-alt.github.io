def get_receipt(nakup, width=40):
    out_str = " ÚČTENKA ".center(width, "=") + "\n"

    for key, val in nakup.items():
        fill_width = width - len(key)
        out_str += f"{key}{val:.>{fill_width}.2f}\n"

    out_str += (
        f"{'-':->{width}s}\n"
        f"Celkem (Kč)\n"
        f"{sum(nakup.values()): >{width}.2f}"
    )
    return out_str


def main():
    nakup = {
        "rohliky": 20,
        "salam": 23.9,
        "maslo": 62.5,
        "tuřín": 1348
    }


    print(get_receipt(nakup, 51))


if __name__ == "__main__":
    main()

