function() {
  ​​// 클릭 이벤트를 통해 발생한 요소를 대상으로 합니다.
  ​​var targetElement = {{Click Element}};
  
  ​​// 'gtm_example' 속성이 있는지, 또는 가장 가까운 상위 요소에 'slot' 속성이 있는지 확인합니다.
  ​​var gtagElement = targetElement.closest('[gtm_example]');
  ​​if (gtagElement) {
  ​​​​// 'gtm_example' 속성 값을 반환합니다.
  ​​​​return gtagElement.getAttribute('gtm_example');
  ​​} else {
  ​​​​// 만약 'gtm_example' 속성이 없다면, undefined를 반환합니다.
  ​​​​return undefined;
  ​​}
}
