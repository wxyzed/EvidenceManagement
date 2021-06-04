pragma solidity ^0.5.16;

// Creating a Smart Contract
contract Evidence{

// Structure of evidence
struct Evidence{
	
	// State variables
	int evid;
	string name;
	string owner;
	string location;
	string myHash;
}

Evidence []evds;

// Function to add evidence details
function addEvidence(
	int evid, string memory name,
	string memory owner,
	string memory location,
	string memory myHash
) public{
	Evidence memory e
		=Evidence(evid,
				name,
				owner,
				location,
				myHash);
	evds.push(e);
}

// Function to get details of evidence
function getEvidence(
	int evid
) public view returns(
	string memory,
	string memory,
	string memory,
	string memory){
	uint i;
	for(i=0;i<evds.length;i++)
	{
		Evidence memory e
			=evds[i];
		
		// Looks for a matching
		// Evidence id
		if(e.evid==evid)
		{
				return(e.name,
					e.owner,
					e.location,
					e.myHash);
		}
	}
	
	// If evidence exists id is not present it returns Not Found
	return("Not Found",
			"Not Found",
			"Not Found",
			"Not Found");
    }
}
