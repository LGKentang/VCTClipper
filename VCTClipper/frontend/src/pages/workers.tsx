import { useEffect, useState } from "react";
import Paper from "../components/root/paper";
import "../../public/css/pages/workers.scss";
import { HiWrenchScrewdriver } from "react-icons/hi2";
import ModalButton from "../components/button/modal_button";
import { MdPersonAddAlt } from "react-icons/md";
import { saveWorker } from "../controller/worker_controller";
import { FaCircle } from "react-icons/fa6";
import ToggleButton from "../components/button/toggle_button";
import NodeDetails from "../components/data/node_details";

const Workers = () => {
  const [name, setName] = useState("");
  const [channelHandle, setChannelHandle] = useState("");
  const [mediaType, setMediaType] = useState("Youtube");
  const [workers, setWorkers] = useState<Worker[]>([]);
  const [channelData, setChannelData] = useState<ChannelData | null>(null);
  const [debounceTimeout, setDebounceTimeout] = useState<NodeJS.Timeout | null>(
    null
  );

  const fetchWorkers = async () => {
    try {
      const response = await fetch("http://localhost:5000/get_worker/all");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      console.log(data);
      setWorkers(data);
    } catch (error) {
      console.error("Error fetching worker data:", error);
    }
  };

  useEffect(() => {
    if (!channelHandle) return;

    if (debounceTimeout) {
      clearTimeout(debounceTimeout);
    }

    const timeout = setTimeout(() => {
      const fetchChannelData = async () => {
        const response = await fetch(
          `http://localhost:5000/get_channel_by_handle/${
            channelHandle.startsWith("@") ? "" : "@"
          }${channelHandle}`
        );
        const data = await response.json();
        console.log(data);
        setChannelData(data);
      };
      fetchChannelData();
    }, 500);

    setDebounceTimeout(timeout);

    return () => {
      if (timeout) {
        clearTimeout(timeout);
      }
    };
  }, [channelHandle]);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    await saveWorker(name, channelHandle, mediaType);
    await fetchWorkers(); 
    setName(""); 
    setChannelHandle("");
    setMediaType("Youtube");
  };

  useEffect(() => {
    fetchWorkers(); 
  }, []);

  return (
    <>
      <div className="worker-header">
        <HiWrenchScrewdriver size={20} />
        <h2>Workers</h2>
      </div>

      <div className="worker-divider">
        <Paper padding={"1rem"}>
          <div className="worker-ongoing">
            <div>
              <h2>Nodes</h2>
            </div>
            <hr style={{ width: "100%" }} />

            <div className="worker-ongoing-datas">
              {workers.map((worker, index) => (
                <NodeDetails key={index} worker={worker} />
              ))}
            </div>
          </div>
        </Paper>

        <Paper margin={"0"} padding={"1rem"}>
          <div className="worker-status">
            <h2>Status</h2>
          </div>
        </Paper>
      </div>

      <div className="add-worker-button">
        <ModalButton
          button_content={<MdPersonAddAlt size={20} />}
          content={
            <>
              <Paper
                padding={"1rem"}
                style={{
                  background: `linear-gradient(135deg, #161616, ${
                    mediaType === "Youtube" ? "#9518182a" : "#7e18952a"
                  })`,
                }}
              >
                <div
                  style={{
                    zIndex: 1,
                    position: "absolute",
                    bottom: `${mediaType === "Youtube" ? "-60px" : "-20px"}`,
                    left: `${mediaType === "Youtube" ? "-10px" : "-0px"}`,
                    width: `${mediaType === "Youtube" ? "150px" : "130px"}`,
                    height: `${mediaType === "Youtube" ? "150px" : "130px"}`,
                    backgroundImage: `url('./images/${
                      mediaType === "Youtube" ? "youtube" : "twitch"
                    }.png')`,
                    backgroundRepeat: "no-repeat",
                    backgroundSize: "contain",
                    transform: "rotate(-12deg)",
                  }}
                />

                <div className="channel-data-overlay">
                  {channelData && (
                    <>
                      <img
                        className="circular-img"
                        src={channelData.img_url}
                        // onError={(e) => console.log(e)}
                      />
                      {channelData.name}
                    </>
                  )}
                </div>

                <div className="worker-add">
                  <h2>Add New Worker</h2>

                  <form onSubmit={handleSubmit}>
                    <div className="input-field">
                      <h3>Name</h3>
                      <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                      />
                    </div>

                    <div className="input-field">
                      <h3>Channel Handle</h3>
                      <input
                        type="text"
                        value={channelHandle}
                        onChange={(e) => setChannelHandle(e.target.value)}
                        required
                      />
                    </div>

                    <div className="input-field">
                      <h3>Media Type</h3>
                      <select
                        value={mediaType}
                        onChange={(e) => setMediaType(e.target.value)}
                        required
                      >
                        <option value="Youtube">Youtube</option>
                        <option value="Twitch">Twitch</option>
                      </select>
                    </div>

                    <div className="save-worker">
                      <button type="submit">Save Worker</button>
                    </div>
                  </form>
                </div>
              </Paper>
            </>
          }
        />
      </div>
    </>
  );
};

export default Workers;
