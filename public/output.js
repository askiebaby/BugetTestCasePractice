module.exports = {
  outputChar: function(input) {
    const splitedInputArr = inputSpliter(input);
    const repeatArr = repeatInput(splitedInputArr);

    return repeatArr.join('-');
  },
};

const inputSpliter = function(input) {
  return input.split('');
};

const repeatInput = function(inputArr) {
  return inputArr.map((input, inputIndex) => {
    let str = '';

    for (let i = 0; i <= inputIndex; i++) {
      str += lowerInput(input);
    }

    return upperFirstStr(str);
  });
};

const upperFirstStr = function(input) {
  let FirstUpperStr = input[0].toUpperCase() + input.substr(1, input.length);

  return isEnglishChar(input) ? FirstUpperStr : input;
};

const lowerInput = function(input) {
  return isEnglishChar(input) ? input.toLowerCase() : input;
};

const isEnglishChar = function(input) {
  let english = /^[a-zA-Z]*$/;
  return english.test(input);
};
