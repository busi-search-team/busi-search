const parse = require("pg-connection-string").parse;
const { Pool } = require("pg");
//const { v4: uuidv4 } = require("uuid");
const cat = "Indian Restaurant";
const lat = 0.00000
const lon = 0.00000

function distance(lat1, lon1, lat2, lon2) {
  var p = 0.017453292519943295;    // Math.PI / 180
  var c = Math.cos;
  var a = 0.5 - c((lat2 - lat1) * p)/2 + 
          c(lat1 * p) * c(lat2 * p) * 
          (1 - c((lon2 - lon1) * p))/2;

  return 12742 * Math.asin(Math.sqrt(a)); 
};

// Run the transactions in the connection pool
(async () => {
  const URI = {
    connectionString: 'postgresql://demonicsandwich:phNrIMo1JCe2Wawz@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/bank?sslmode=verify-full&sslrootcert=$env:appdata/.postgresql/root.crt&options=--cluster%3Dbusi-search-3508'
  };
  //console.log(URI);
  var connectionString;
  // Expand $env:appdata environment variable in Windows connection string
  if (URI.connectionString.includes("env:appdata")) {
    connectionString = await URI.connectionString.replace(
      "$env:appdata",
      process.env.APPDATA
    );
  }
  // Expand $HOME environment variable in UNIX connection string
  else if (URI.connectionString.includes("HOME")){
    connectionString = await URI.connectionString.replace(
      "$HOME",
      process.env.HOME
    );
  }
  var config = parse(connectionString);
  config.port = 26257;
  config.database = "bank";
  const pool = new Pool(config);

  // Connect to database
  const client = await pool.connect();
  

  // Initialize table in transaction retry wrapper
  var locations_e = []
  const locations = await client.query(`SELECT * FROM locations WHERE category = '${cat}';`);
  //console.log(locations.type);

  for (let i = 0;i<locations.rows.length;i++) {
    console.log(locations.rows[i].name);
    if (distance(lat, lon, locations.rows[i].lat, locations.rows[i].lon) <= 25){
      locations_e.push(locations.rows[i].place_id);
    }
  };

  

  // Exit program
  process.exit();
})().catch((err) => console.log(err.stack));
