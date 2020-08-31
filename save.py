import csv


def save_to_csv(items, **kwargs):
    filename = kwargs.get("filename")

    with open(f"download/{filename}", 'w', newline='\n', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["region", "title", "price",
                         "link", "img", "like", "chat"])
        for item in items:
            writer.writerow((list)(item.values()))
    return
