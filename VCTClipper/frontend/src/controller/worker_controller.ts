export async function saveWorker(name: string, channelHandle: string, mediaType: string) {
    try {
        const response = await fetch('http://localhost:5000/add_worker', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, channelHandle, mediaType }),
        });

        if (!response.ok) {
            let errorDetails;
            try {
                errorDetails = await response.json();
            } catch (jsonError) {
                errorDetails = await response.text(); 
            }

            throw new Error(`HTTP error! Status: ${response.status}. Details: ${errorDetails}`);
        }

        const result = await response.json();
        console.log(result.message); 
    } catch (error) {
        console.error('Error:', (error as Error).message);
    }
}

function get_worker_by_uuid(uuid:string){
    
}
