const outputs = require('../output.js');

describe('Output character', () => {
  test('Input_EqualTo_Output', () => {
    const output = outputs.outputChar('A');
    expect(output).toBe('A');

    const output2 = outputs.outputChar('');
    expect(output2).toBe('');
  });

  test('Input_DashRepeat', () => {
    const output = outputs.outputChar('哈囉');
    expect(output).toBe('哈-囉囉');
  });

  test('Input_Uppercase', () => {
    const output = outputs.outputChar('a');
    expect(output).toBe('A');
  });

  test('Input_FirstUppercase', () => {
    const output = outputs.outputChar('ab');
    expect(output).toBe('A-Bb');
  });

  test('Input_abC', () => {
    const output = outputs.outputChar('abC');
    expect(output).toBe('A-Bb-Ccc');
  });
});
