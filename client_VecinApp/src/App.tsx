import { TestButton } from "@/components/TestButton";

function App() {
  return (
    <div className="min-h-screen bg-grayLight dark:bg-grayDark">
      <div className="container-custom py-8">
        <h1 className="text-3xl font-bold text-primary mb-4">VecinApp</h1>
        <p className="text-grayDark dark:text-grayLight">
          Configuración inicial completada ✅
        </p>
        <TestButton />
      </div>
    </div>
  );
}

export default App;
