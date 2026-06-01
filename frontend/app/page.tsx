// "use client";

// import { useState } from "react";

// export default function Home() {

//   const [prompt, setPrompt] = useState("");

//   const [result, setResult] = useState<any>(null);

//   const generateApp = async () => {

//     const response = await fetch(
//       "http://127.0.0.1:8001/api/generate",
//       {
//         method: "POST",

//         headers: {
//           "Content-Type": "application/json",
//         },

//         body: JSON.stringify({
//           prompt,
//         }),
//       }
//     );
//     console.log(response);
//     const data = await response.json();
//     console.log(data);
//     setResult(data);
//   };

//   return (

//     <div className="p-10">

//       <h1 className="text-3xl font-bold mb-6">
//         AI App Compiler
//       </h1>

//       <textarea
//         className="border p-3 w-full h-40"
//         placeholder="Enter app idea..."
//         value={prompt}
//         onChange={(e) => setPrompt(e.target.value)}
//       />

//       <button
//         onClick={generateApp}
//         className="bg-black text-white px-6 py-3 mt-4"
//       >
//         Generate
//       </button>

//       {result && (

//         <pre className="mt-8 bg-gray-100 text-black p-5 overflow-auto">
//           {JSON.stringify(result, null, 2)}

//         </pre>
//       )}
//       {result && (

//   <div className="mt-8 p-6 border rounded-lg bg-white text-black shadow">

//     <h1 className="text-3xl font-bold mb-6">
//       🚀 AI App Compiler Result
//     </h1>
//     <div className="mb-6 p-4 border rounded bg-green-50">

//   <h2 className="text-xl font-semibold">
//     ⚙️ Pipeline Summary
//   </h2>

//   <p>
//     Entities Generated: {result.schema.entities?.length}
//   </p>

//   <p>
//     Pages Generated: {result.appspec.pages?.length}
//   </p>

//   <p>
//     API Endpoints: {result.appspec.apiEndpoints?.length}
//   </p>

//   <p>
//     Roles: {result.appspec.authRules?.roles?.length}
//   </p>

//  </div>
//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">📌 App Overview</h2>

//       <p>
//         <strong>App Type:</strong> {result.intent.appType}
//       </p>

//       <p>
//         <strong>App Name:</strong> {result.intent.appName || "Generated App"}
//       </p>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">⚡ Features</h2>

//       <ul className="list-disc ml-6">
//         {result.intent.features?.map((feature: string, index: number) => (
//           <li key={index}>{feature}</li>
//         ))}
//       </ul>
//     <div className="mb-6">
//   <h2 className="text-xl font-semibold">
//     📦 Database Schema
//   </h2>
// </div>
//   {result.schema.entities?.map(
//     (entity: any, index: number) => (
//       <div
//         key={index}
//         className="border rounded p-4 my-3 bg-gray-50"
//       >
//         <h3 className="font-bold text-lg">
//           {entity.name}
//         </h3>

//         <p className="text-sm text-gray-600">
//           Table: {entity.tableName}
//         </p>

//         <div className="mt-2">
//           <strong>Fields:</strong>

//           <ul className="list-disc ml-6">
//             {entity.fields?.map(
//               (field: string, idx: number) => (
//                 <li key={idx}>{field}</li>
//               )
//             )}
//           </ul>
//         </div>
//       </div>
//     )
//   )}
// </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">🔌 Requested Integrations</h2>

//       <ul className="list-disc ml-6">
//         {result.intent.integrations_requested?.map(
//           (integration: string, index: number) => (
//             <li key={index}>{integration}</li>
//           )
//         )}
//       </ul>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">📝 Assumptions</h2>

//       <ul className="list-disc ml-6">
//         {result.intent.assumptions?.map(
//           (assumption: string, index: number) => (
//             <li key={index}>{assumption}</li>
//           )
//         )}
//       </ul>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">📄 Generated Pages</h2>

//       <ul className="list-disc ml-6">
//         {result.appspec.pages?.map((page: any, index: number) => (
//           <li key={index}>{page.name}</li>
//         ))}
//       </ul>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">🔗 API Endpoints</h2>

//       <ul className="list-disc ml-6">
//         {result.appspec.apiEndpoints?.map((api: any, index: number) => (
//           <li key={index}>
//             {api.method} - {api.path}
//           </li>
//         ))}
//       </ul>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">🔌 Integration Hooks</h2>

//       <ul className="list-disc ml-6">
//         {result.appspec.integrationHooks?.map(
//           (item: any, index: number) => (
//             <li key={index}>{item.integration}</li>
//           )
//         )}
//       </ul>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">⚙️ Workflow Stubs</h2>

//       <ul className="list-disc ml-6">
//         {result.appspec.workflowStubs?.map(
//           (workflow: any, index: number) => (
//             <li key={index}>{workflow.name}</li>
//           )
//         )}
//       </ul>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">🔐 Roles</h2>

//       <ul className="list-disc ml-6">
//         {result.appspec.authRules?.roles?.map(
//           (role: string, index: number) => (
//             <li key={index}>{role}</li>
//           )
//         )}
//       </ul>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">✅ Validation Status</h2>

//       <p>
//         {result.validation.success
//           ? "✅ Passed"
//           : "❌ Failed"}
//       </p>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">🛠 Repair Log</h2>

//       <p>
//         {result.repair_log?.length > 0
//           ? result.repair_log.length + " repairs applied"
//           : "No repairs needed"}
//       </p>
//     </div>

//     <div className="mb-6">
//       <h2 className="text-xl font-semibold">💰 Cost Breakdown</h2>

//       <p>
//         Intent Extraction: $
//         {result.cost_breakdown.intent_extraction}
//       </p>

//       <p>
//         Schema Generation: $
//         {result.cost_breakdown.schema_generation}
//       </p>

//       <p>
//         AppSpec Generation: $
//         {result.cost_breakdown.appspec_generation}
//       </p>
//     </div>

//     <div>
//       <h2 className="text-xl font-semibold">
//         ⏱ Performance Metrics
//       </h2>

//       <p>
//         Intent Extraction:
//         {" "}
//         {result.latency.intent_extraction}s
//       </p>

//       <p>
//         Schema Generation:
//         {" "}
//         {result.latency.schema_generation}s
//       </p>

//       <p>
//         AppSpec Generation:
//         {" "}
//         {result.latency.appspec_generation}
//       </p>
//     </div>

//   </div>

//  );
// }

      
   








// "use client";

// import { useState } from "react";

// export default function Home() {
//   const [prompt, setPrompt] = useState("");
//   const [result, setResult] = useState<any>(null);

//   const generateApp = async () => {
//     const response = await fetch("http://127.0.0.1:8001/api/generate", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({
//         prompt,
//       }),
//     });
//     console.log(response);
//     const data = await response.json();
//     console.log(data);
//     setResult(data);
//   };

//   return (
//     <div className="p-10">
//       <h1 className="text-3xl font-bold mb-6">AI App Compiler</h1>

//       <textarea
//         className="border p-3 w-full h-40"
//         placeholder="Enter app idea..."
//         value={prompt}
//         onChange={(e) => setPrompt(e.target.value)}
//       />

//       <button
//         onClick={generateApp}
//         className="bg-black text-white px-6 py-3 mt-4"
//       >
//         Generate
//       </button>

//       {result && (
//         <pre className="mt-8 bg-gray-100 text-black p-5 overflow-auto">
//           {JSON.stringify(result, null, 2)}
//         </pre>
//       )}

//       {result && (
//         <div className="mt-8 p-6 border rounded-lg bg-white text-black shadow">
//           <h1 className="text-3xl font-bold mb-6">🚀 AI App Compiler Result</h1>

//           <div className="mb-6 p-4 border rounded bg-green-50">
//             <h2 className="text-xl font-semibold">⚙️ Pipeline Summary</h2>
//             <p>Entities Generated: {result.schema.entities?.length}</p>
//             <p>Pages Generated: {result.appspec.pages?.length}</p>
//             <p>API Endpoints: {result.appspec.apiEndpoints?.length}</p>
//             <p>Roles: {result.appspec.authRules?.roles?.length}</p>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">📌 App Overview</h2>
//             <p>
//               <strong>App Type:</strong> {result.intent.appType}
//             </p>
//             <p>
//               <strong>App Name:</strong> {result.intent.appName || "Generated App"}
//             </p>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">⚡ Features</h2>
//             <ul className="list-disc ml-6">
//               {result.intent.features?.map((feature: string, index: number) => (
//                 <li key={index}>{feature}</li>
//               ))}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">📦 Database Schema</h2>
//             {result.schema.entities?.map((entity: any, index: number) => (
//               <div key={index} className="border rounded p-4 my-3 bg-gray-50">
//                 <h3 className="font-bold text-lg">{entity.name}</h3>
//                 <p className="text-sm text-gray-600">Table: {entity.tableName}</p>
//                 <div className="mt-2">
//                   <strong>Fields:</strong>
//                   <ul className="list-disc ml-6">
//                     {entity.fields?.map((field: string, idx: number) => (
//                       <li key={idx}>{field}</li>
//                     ))}
//                   </ul>
//                 </div>
//               </div>
//             ))}
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">🔌 Requested Integrations</h2>
//             <ul className="list-disc ml-6">
//               {result.intent.integrations_requested?.map(
//                 (integration: string, index: number) => (
//                   <li key={index}>{integration}</li>
//                 )
//               )}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">📝 Assumptions</h2>
//             <ul className="list-disc ml-6">
//               {result.intent.assumptions?.map(
//                 (assumption: string, index: number) => (
//                   <li key={index}>{assumption}</li>
//                 )
//               )}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">📄 Generated Pages</h2>
//             <ul className="list-disc ml-6">
//               {result.appspec.pages?.map((page: any, index: number) => (
//                 <li key={index}>{page.name}</li>
//               ))}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">🔗 API Endpoints</h2>
//             <ul className="list-disc ml-6">
//               {result.appspec.apiEndpoints?.map((api: any, index: number) => (
//                 <li key={index}>
//                   {api.method} - {api.path}
//                 </li>
//               ))}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">🔌 Integration Hooks</h2>
//             <ul className="list-disc ml-6">
//               {result.appspec.integrationHooks?.map(
//                 (item: any, index: number) => (
//                   <li key={index}>{item.integration}</li>
//                 )
//               )}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">⚙️ Workflow Stubs</h2>
//             <ul className="list-disc ml-6">
//               {result.appspec.workflowStubs?.map(
//                 (workflow: any, index: number) => (
//                   <li key={index}>{workflow.name}</li>
//                 )
//               )}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">🔐 Roles</h2>
//             <ul className="list-disc ml-6">
//               {result.appspec.authRules?.roles?.map(
//                 (role: string, index: number) => (
//                   <li key={index}>{role}</li>
//                 )
//               )}
//             </ul>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">✅ Validation Status</h2>
//             <p>{result.validation.success ? "✅ Passed" : "❌ Failed"}</p>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">🛠 Repair Log</h2>
//             <p>
//               {result.repair_log?.length > 0
//                 ? result.repair_log.length + " repairs applied"
//                 : "No repairs needed"}
//             </p>
//           </div>

//           <div className="mb-6">
//             <h2 className="text-xl font-semibold">💰 Cost Breakdown</h2>
//             <p>Intent Extraction: ${result.cost_breakdown.intent_extraction}</p>
//             <p>Schema Generation: ${result.cost_breakdown.schema_generation}</p>
//             <p>AppSpec Generation: ${result.cost_breakdown.appspec_generation}</p>
//           </div>

//           <div>
//             <h2 className="text-xl font-semibold">⏱ Performance Metrics</h2>
//             <p>Intent Extraction: {result.latency.intent_extraction}s</p>
//             <p>Schema Generation: {result.latency.schema_generation}s</p>
//             <p>AppSpec Generation: {result.latency.appspec_generation}</p>
//           </div>
//         </div>
//       )}
//     </div>
//   );
// }



"use client";

import { useState } from "react";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState<any>(null);
  const [logs, setLogs] = useState<string[]>([]);

  // const generateApp = async () => {
  //   setLogs([]);
  //   const eventSource = new EventSource("http://127.0.0.1:8001/api/generate-stream");
  //   eventSource.onmessage = (event) => {
  //     console.log("SSE:", event.data);
  //     setLogs((prev) => [...prev, event.data]);
  //   };
  //   eventSource.onerror = () => {
  //     // setResult(data);
  //     eventSource.close();
  //   };
  //   const response = await fetch("http://127.0.0.1:8001/api/generate", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify({
  //       prompt,
  //     }),
  //   });
  //   console.log(response);
  //   const data = await response.json();
  //   console.log(data);
  //   setResult(data);
  //   eventSource.close();
  // };
  const generateApp = async () => {

  setLogs([]);
  setResult(null);

  const response = await fetch(
    "http://127.0.0.1:8001/api/generate-stream",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt,
      }),
    }
  );
  if (!response.ok) {

  setLogs((prev) => [
    ...prev,
    `❌ Request Failed (${response.status})`
  ]);

  return;
}
if (!response.body) {

  setLogs((prev) => [
    ...prev,
    "❌ No response body received"
  ]);

  return;
}

  if (!response.body) return;

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  let buffer = "";

  while (true) {

    const { done, value } =
      await reader.read();

    if (done) break;

    buffer += decoder.decode(value, {
      stream: true,
    });

    const events =
      buffer.split("\n\n");

    buffer = events.pop() || "";

    for (const event of events) {

      const lines =
        event.split("\n");

      let eventType = "message";
      let eventData = "";

      for (const line of lines) {

        if (
          line.startsWith("event:")
        ) {
          eventType = line
            .replace("event:", "")
            .trim();
        }

        if (
          line.startsWith("data:")
        ) {
          eventData += line
            .replace("data:", "")
            .trim();
        }
      }

      console.log(
        "EVENT:",
        eventType,
        eventData
      );

      if (
        eventType === "message"
      ) {
        setLogs((prev) => [
          ...prev,
          eventData,
        ]);
      }

      if (
        eventType === "result"
      ) {
        setResult(
          JSON.parse(eventData)
        );
      }

      if (
        eventType === "error"
      ) {
        setLogs((prev) => [
          ...prev,
          `❌ ${eventData}`,
        ]);
      }
    }
  }
};
  const getFieldType = (field: any) => {
  if (!field?.type) return "-";

  if (field.type.startsWith("Foreign Key")) {
    return "Foreign Key";
  }

  return field.type;
};

// const getFieldDetails = (field: any) => {
//   if (!field?.type) return "-";

//   if (field.type.startsWith("Foreign Key")) {
//     return field.type
//       .replace("Foreign Key (", "")
//       .replace(")", "");
//   }

//   if (field.type === "Enum" && field.values) {
//     return field.values.join(", ");
//   }

//   return "-";
// };
const getFieldDetails = (field: any) => {
  if (field.references) {
    return `References ${field.references}`;
  }

  if (field.values?.length) {
    return field.values.join(", ");
  }

  return "-";
};
  
  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">AI App Compiler</h1>

      <textarea
        className="border p-3 w-full h-40"
        placeholder="Enter app idea..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        onClick={generateApp}
        className="bg-black text-white px-6 py-3 mt-4"
      >
        Generate
      </button>
       {logs.length > 0 && (
  <div className="mt-6 p-4 border rounded bg-white text-black shadow">
    <h2 className="font-bold text-xl mb-3 text-black">
      Pipeline Progress
    </h2>

    {logs.map((log, index) => (
      <div
        key={index}
        className="py-2 border-b text-black font-medium"
      >
        {log}
      </div>
    ))}
  </div>
)}
{result?.success === false && (
  <div className="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
    {result.error}
  </div>
)}
       {result && (
        <div className="mt-8 p-6 border rounded-lg bg-white text-black shadow">
          <h1 className="text-3xl font-bold mb-6">🚀 AI App Compiler Result</h1>

          <div className="mb-6 p-4 border rounded bg-green-50">
            <h2 className="text-xl font-semibold">⚙️ Pipeline Summary</h2>
            <p>Entities Generated: {result?.schema?.entities?.length??0}</p>
            <p>Pages Generated: {result?.appspec?.pages?.length??0}</p>
            <p>API Endpoints: {result?.appspec?.apiEndpoints?.length??0}</p>
            <p>Roles: {result?.appspec?.authRules?.roles?.length??0}</p>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">📌 App Overview</h2>
            <p>
              <strong>App Type:</strong> {result.intent.appType}
            </p>
            <p>
              <strong>App Name:</strong> {result.intent.appName || "Generated App"}
            </p>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">⚡ Features</h2>
            <ul className="list-disc ml-6">
              {result.intent.features?.map((feature: string, index: number) => (
                <li key={index}>{feature}</li>
              ))}
            </ul>
          </div>

          <div className="mb-8">
  <h2 className="text-2xl font-bold mb-4">
    📦 Database Schema
  </h2>

  {result.schema.entities?.map((entity: any, index: number) => (
    <div
      key={index}
      className="mb-6 border rounded-lg overflow-hidden"
    >
      <div className="bg-gray-100 p-4">
        <h3 className="font-bold text-lg">
          {entity.name}
        </h3>
        
        <p className="text-sm text-gray-600">
          Table: {entity.tableName}
        </p>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-gray-200">
              <th className="border p-2 text-left">
                Field
              </th>

              <th className="border p-2 text-left">
                Type
              </th>

              <th className="border p-2 text-left">
                Nullable
              </th>

              <th className="border p-2 text-left">
                Unique
              </th>

              <th className="border p-2 text-left">
                Details
              </th>
            </tr>
          </thead>

          <tbody>
            {entity.fields?.map(
              (field: any, idx: number) => (
                <tr key={idx}>
                  <td className="border p-2">
  {typeof field === "string" ? field : field.name}
</td>

                  <td className="border p-2">
  {typeof field === "string"
    ? "String"
    : getFieldType(field)}
</td>

                  <td className="border p-2">
                    {field.nullable ? "Yes" : "No"}
                  </td>

                  <td className="border p-2">
                    {field.unique ? "Yes" : "No"}
                  </td>

                 <td className="border p-2">
  {typeof field === "string"
    ? "-"
    : getFieldDetails(field)}
</td>
                </tr>
              )
            )}
          </tbody>
        </table>
      </div>
    </div>
  ))}
</div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">🔌 Requested Integrations</h2>
            <ul className="list-disc ml-6">
              {result.intent.integrations_requested?.map(
                (integration: string, index: number) => (
                  <li key={index}>{integration}</li>
                )
              )}
            </ul>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">📝 Assumptions</h2>
            <ul className="list-disc ml-6">
              {result.intent.assumptions?.map(
                (assumption: string, index: number) => (
                  <li key={index}>{assumption}</li>
                )
              )}
            </ul>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">📄 Generated Pages</h2>
            <div className="overflow-x-auto">
  <table className="w-full border">
    <thead>
      <tr>
        <th className="border p-2">Page</th>
        <th className="border p-2">Route</th>
        <th className="border p-2">Entity</th>
      </tr>
    </thead>

    <tbody>
      {result.appspec.pages?.map(
        (page: any, index: number) => (
          <tr key={index}>
            <td className="border p-2">
              {page.name}
            </td>

            <td className="border p-2">
              {page.route}
            </td>

            <td className="border p-2">
              {page.entity}
            </td>
          </tr>
        )
      )}
    </tbody>
  </table>
</div>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">🔗 API Endpoints</h2>
            <table className="w-full border">
  <thead>
    <tr>
      <th className="border p-2">Method</th>
      <th className="border p-2">Endpoint</th>
      <th className="border p-2">Entity</th>
    </tr>
  </thead>

  <tbody>
    {result.appspec.apiEndpoints?.map(
      (api: any, index: number) => (
        <tr key={index}>
          <td className="border p-2">
            {api.method}
          </td>

          <td className="border p-2">
            {api.path}
          </td>

          <td className="border p-2">
            {api.entity}
          </td>
        </tr>
      )
    )}
  </tbody>
</table>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">🔌 Integration Hooks</h2>
            <div className="overflow-x-auto">
  <table className="w-full border">
    <thead>
      <tr>
        <th className="border p-2">
          Integration
        </th>

        <th className="border p-2">
          Action
        </th>
      </tr>
    </thead>

    <tbody>
      {result.appspec.integrationHooks?.map(
        (item: any, index: number) => (
          <tr key={index}>
            <td className="border p-2">
              {item.integration}
            </td>

            <td className="border p-2">
              {item.action}
            </td>
          </tr>
        )
      )}
    </tbody>
  </table>
</div>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">⚙️ Workflow Stubs</h2>
            <div className="overflow-x-auto">
  <table className="w-full border">
    <thead>
      <tr>
        <th className="border p-2">
          Workflow
        </th>

        <th className="border p-2">
          Trigger Entity
        </th>

        <th className="border p-2">
          Integration
        </th>

        <th className="border p-2">
          Action
        </th>
      </tr>
    </thead>

    <tbody>
      {result.appspec.workflowStubs?.map(
        (workflow: any, index: number) => (
          <tr key={index}>
            <td className="border p-2">
              {workflow.name}
            </td>

            <td className="border p-2">
              {workflow.triggerEntity}
            </td>

            <td className="border p-2">
              {workflow.integration}
            </td>

            <td className="border p-2">
              {workflow.action}
            </td>
          </tr>
        )
      )}
    </tbody>
  </table>
</div>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">🔐 Roles</h2>
            <div className="overflow-x-auto">
  <table className="w-full border">
    <thead>
      <tr>
        <th className="border p-2">Role</th>
      </tr>
    </thead>

    <tbody>
      {result.appspec.authRules?.roles?.map(
        (role: string, index: number) => (
          <tr key={index}>
            <td className="border p-2">
              {role}
            </td>
          </tr>
        )
      )}
    </tbody>
  </table>
</div>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">✅ Validation Status</h2>
            <p>{result.validation.success ? "✅ Passed" : "❌ Failed"}</p>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">🛠 Repair Log</h2>
            <p>
              {result.repair_log?.length > 0
                ? result.repair_log.length + " repairs applied"
                : "No repairs needed"}
            </p>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold">💰 Cost Breakdown</h2>
            <p>Intent Extraction: ${result.cost_breakdown.intent_extraction}</p>
            <p>Schema Generation: ${result.cost_breakdown.schema_generation}</p>
            <p>AppSpec Generation: ${result.cost_breakdown.appspec_generation}</p>
          </div>

          <div>
            <h2 className="text-xl font-semibold">⏱ Performance Metrics</h2>
            <p>Intent Extraction: {result.latency.intent_extraction}s</p>
            <p>Schema Generation: {result.latency.schema_generation}s</p>
            <p>AppSpec Generation: {result.latency.appspec_generation}</p>
          </div>
          <div className="mb-8">
  <h2 className="text-xl font-bold mb-4">
    📊 Trace Log
  </h2>

  <ul className="space-y-2">
    {result.trace_log?.map(
      (log: string, index: number) => (
        <li key={index}>
          ✅ {log}
        </li>
      )
    )}
  </ul>
</div>
        </div>
      )}
    </div>
  );
}