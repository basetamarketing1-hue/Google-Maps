import requests
import csv

def find_places(api_key, city_name):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": city_name,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = data.get("results", [])

    filtered = []
    for place in results:
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            "place_id": place["place_id"],
            "fields": "name,formatted_address,geometry,international_phone_number,website",
            "key": api_key
        }
        det = requests.get(details_url, params=details_params).json()
        det_result = det.get("result", {})
        phone = det_result.get("international_phone_number")
        website = det_result.get("website")

        if not phone and not website:
            filtered.append([
                det_result.get("name"),
                det_result.get("formatted_address"),
                det_result.get("geometry", {}).get("location", {}).get("lat"),
                det_result.get("geometry", {}).get("location", {}).get("lng"),
                place["place_id"]
            ])

    # Save to CSV
    with open("missing_contact_places.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Address", "Lat", "Lng", "Place ID"])
        writer.writerows(filtered)

    print("Saved:", len(filtered), "places without contact data.")
