# ArXiv

## Description

ArXiv is a Node.js module for searching ArXiv for articles based on a query.

## Installation

Make sure you have [Node.js](https://nodejs.org/) installed.

```bash
npm install
```

## Usage

```javascript
const { searchArXiv } = require('arxiv');

const query = 'your search query';
searchArXiv(query)
  .then((results) => {
    // Process and use the search results
    console.log(results);
  })
  .catch((error) => {
    console.error(error.message);
  });
```

## Parameters Returned

- **title**
- **id**
- **published**
- **summary**
- **link**

## Example Usage

```javascript
const { searchArXiv } = require('arxiv');

const query = 'Science';

searchArXiv(query)
  .then((results) => {
    // Process and use the search results
    console.log(results);
  })
  .catch((error) => {
    console.error(error.message);
  });
```

### Example Response

```json
[
  {
    "title": "Sample Article Title",
    "id": "http://arxiv.org/abs/1234.5678",
    "published": "2022-01-14T12:34:56Z",
    "summary": "This is a sample article summary.",
    "link": "http://arxiv.org/abs/1234.5678"
  },
]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
