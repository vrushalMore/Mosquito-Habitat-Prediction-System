import { useState } from "react";

const questions = [
  { text: "What is the daily minimum temperature?", options: ["Low", "Medium", "High"], key: "daily_min_temp" },
  { text: "What is the daily maximum temperature?", options: ["Low", "Medium", "High"], key: "daily_max_temp" },
  { text: "What is the daily average temperature?", options: ["Low", "Medium", "High"], key: "daily_avg_temp" },
  { text: "How much total precipitation is there?", options: ["Low", "Medium", "High"], key: "total_precipitation" },
  { text: "What is the relative humidity level?", options: ["Low", "Medium", "High"], key: "relative_humidity" },
  { text: "Are there any water bodies in the area?", options: ["Yes", "No"], key: "water_bodies" },
  { text: "What is the population density?", options: ["Low", "Medium", "High"], key: "population_density" },
  { text: "How long is the day?", options: ["Low", "Medium", "High"], key: "day_length" },
  { text: "Is the area urban or rural?", options: ["Urban", "Rural"], key: "urban_rural_area" },
  { text: "Is the area forested?", options: ["Yes", "No"], key: "forested_area" },
  { text: "Is there a crop-growing area?", options: ["Yes", "No"], key: "crop_area" },
  { text: "Is there a grazing land area?", options: ["Yes", "No"], key: "graze_land_area" },
];

export default function Chatbot() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [userData, setUserData] = useState<Record<string, string>>({});
  const [result, setResult] = useState<string | null>(null);

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData),
      })
        .then((response) => response.json())
        .then((data) => setResult(data.prediction === 1 ? "Dangerous" : "Safe"))
        .catch((error) => console.error("Error:", error));
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-black text-white text-center">
      <div className="bg-gray-900 p-8 rounded-lg shadow-lg max-w-sm w-full">
        <h2 className="text-3xl font-bold text-blue-500 mb-5">Chatbot</h2>

        {result ? (
          <h3 className={`text-2xl font-bold ${result === "Dangerous" ? "text-red-500" : "text-green-500"}`}>
            {result}
          </h3>
        ) : (
          <>
            <p className="text-xl mb-4">{questions[currentQuestion].text}</p>
            <select
              className="w-full p-3 border border-blue-500 rounded bg-gray-700 text-white"
              onChange={(e) => setUserData({ ...userData, [questions[currentQuestion].key]: e.target.value })}
            >
              {questions[currentQuestion].options.map((option) => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
            <button
              className="w-full mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded transition"
              onClick={handleNext}
            >
              Next
            </button>
          </>
        )}
      </div>
    </div>
  );
}
