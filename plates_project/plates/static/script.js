const showInputError = (formElement, inputElement, errorMessage) => {
  const errorElement = formElement.querySelector(`.${inputElement.id}-error`);
  inputElement.classList.add('form__input_type_error');
  errorElement.textContent = errorMessage;
  errorElement.classList.add('form__input-error_active');
};


const setEventListeners = (formElement) => {
  const inputList = Array.from(formElement.querySelectorAll('.form__input'));
  const buttonElement = formElement.querySelector(".form__submit")
  // toggleButtonState (inputList, buttonElement);

  inputList.forEach((inputElement) => {
    inputElement.addEventListener('input', function () {

      if(inputElement.value.length > 0) {
        // console.log(inputElement.value.length )
        inputElement.nextElementSibling.classList.add("form__placeholder_is-fixed")
      }
    });
  });
};
const fieldsetList = document.querySelectorAll('.form__set')
    fieldsetList.forEach(fildset => {
      setEventListeners(fildset)
    })

const getPlateBtn = document.querySelector('.btns__btn_get');
const addPlateBtn = document.querySelector('.btns__btn_add');
const resetButton = document.querySelector('.btns__btn_reset');
  const currentPlace = document.querySelector('.container__text')
  const errorMessage = document.querySelector('.error__text')


const url = "http://127.0.0.1:8000"
const tokenTest = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyNDA2NzM1LCJpYXQiOjE2NzM3NjY3MzUsImp0aSI6IjQxNmVmYTYxMTQwMjQwMmNiOThiMTNmN2ZlOGVkZWUyIiwidXNlcl9pZCI6Mn0.AVNmHh5EPfqbtagrAdUB5ncpq3992QCGwg7oyn41V7Q"
let plates = []
let messageError = ""

function getPlates (token, plateId) {
      return fetch(`${url}/plate/get/${plateId}`, {
      method: 'GET',
      headers: {
        authorization: `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    })
    .then((res) => {
      if (res.ok) {
        return res.json()
      } else {

        const errorMessage = res.status == "404" ?
          `Ошибка Api - такого номера нет: ${res.statusText} - ${res.status}` :
          `Ошибка Api - ошибка авторизации: ${res.statusText} - ${res.status}`
        return Promise.reject(errorMessage)
      }
      })
    .then((data) => {
      // console.log(data);
      // plates = [...data];

        return Array.isArray(data) ? [...data] : {...data}
    })
    .catch((err) => {
      messageError = err
      // console.log(err)
      errorMessage.textContent = messageError;
      })
}


async function handleClickGetPlate (event) {
  event.preventDefault();
  errorMessage.textContent = "";
  currentPlace.textContent = "Пусто"
  const inputs = Array.from(document.forms['get-plate'].getElementsByTagName("input"))
  try {
    const plate = await getPlates(inputs[0].value, inputs[1].value)
    if (plate) {
      currentPlace.textContent = Array.isArray(plate) ? plate[0].title : plate.title;
      messageError = "";
      errorMessage.textContent = messageError
    }
  } catch (e) {
    console.log(e)
  }
  finally {
    document.forms['get-plate'].reset()
  }
}

function addPlates (token, plateNum) {
  return fetch(`${url}/plate/add/`, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      title: plateNum
    })
  }).then((res) => {
    if (res.ok) {
      return res.json()
    } else {
      const errorMessage = res.status == "401" ?
       `Ошибка Api - ошибка авторизации: ${res.statusText} - ${res.status}` :
        `Ошибка Api - нужно внести номер в формате а123кр177: ${res.statusText} - ${res.status}`
      return Promise.reject(errorMessage)
    }
  }).then((data) => {
    // console.log(data);
    return {...data}
  }).catch((err) => {
    messageError = err
    // console.log(err)
    errorMessage.textContent = messageError;
  })
}

async function handleClickAddPlate (event) {
  event.preventDefault();
  errorMessage.textContent = "";
  currentPlace.textContent = "Пусто"
  const inputs = Array.from(document.forms['add-plate'].getElementsByTagName("input"))
  console.log(inputs)
  try {
    const plate = await addPlates(inputs[0].value, inputs[1].value)
    if (plate) {
      currentPlace.textContent = plate.title;
      messageError = "RECORDED";
      errorMessage.textContent = messageError
    }
  } catch (e) {
    console.log(e)
  }
  finally {
    document.forms['add-plate'].reset()
  }
}

// listeners
getPlateBtn.addEventListener('submit',() => handleClickGetPlate(event));

addPlateBtn.addEventListener('submit', () => handleClickAddPlate(event));

//
// resetButton.addEventListener('click', function () {
// myCounter.resetCounter()
// });


